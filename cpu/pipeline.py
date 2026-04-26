class PipelineCPU:
    def __init__(self, cpu):
        self.cpu = cpu
        self.program = cpu.program
        self.pc = 0

        self.IF_ID = None
        self.ID_EX = None
        self.EX_MEM = None
        self.MEM_WB = None

        self.cycle = 0
        self.stall = False

        # For table
        self.pipeline_log = {i: [] for i in range(len(self.program))}

    # ---------------- DONE ---------------- #
    def is_done(self):
        return (
            self.pc >= len(self.program)
            and self.IF_ID is None
            and self.ID_EX is None
            and self.EX_MEM is None
            and self.MEM_WB is None
        )

    # ---------------- LOG ---------------- #
    def log(self, idx, stage):
        while len(self.pipeline_log[idx]) < self.cycle - 1:
            self.pipeline_log[idx].append("")
        self.pipeline_log[idx].append(stage)

    # ---------------- FULL HAZARD DETECTION ---------------- #
    def is_hazard(self, instr):
        opcode = instr[0]

        # Source registers
        sources = []
        if opcode in ["ADD", "SUB"]:
            sources = [instr[2], instr[3]]
        elif opcode == "STORE":
            sources = [instr[1]]

        # Check all pipeline stages ahead
        for stage in [self.ID_EX, self.EX_MEM]:
            if not stage:
                continue

            prev = stage[0] if isinstance(stage[0], tuple) else stage

            # Get destination register
            if prev[0] == "LOAD":
                dest = prev[1]
            elif prev[0] == "ALU":
                dest = prev[1]
            else:
                continue

            if dest in sources:
                return True

        return False

    # ---------------- RUN ---------------- #
    def run(self):
        while not self.is_done():
            self.cycle += 1
            print(f"\nCycle {self.cycle}")

            self.write_back()
            self.memory()
            self.execute()
            self.decode()
            self.fetch()

        self.print_table()

    # ---------------- FETCH ---------------- #
    def fetch(self):
        if self.stall:
            return  # freeze IF

        if self.pc < len(self.program):
            instr = self.program[self.pc]
            self.IF_ID = (instr, self.pc)

            print("IF:", instr)
            self.log(self.pc, "IF")

            self.pc += 1

    # ---------------- DECODE ---------------- #
    def decode(self):
        if not self.IF_ID:
            return

        instr, idx = self.IF_ID

        if self.is_hazard(instr):
            print("STALL inserted")
            self.log(idx, "STALL")

            # Insert bubble
            self.ID_EX = None

            # Freeze IF
            self.stall = True
            return

        # Normal flow
        self.ID_EX = (instr, idx)
        print("ID:", instr)
        self.log(idx, "ID")

        self.IF_ID = None
        self.stall = False

    # ---------------- EXECUTE ---------------- #
    def execute(self):
        if not self.ID_EX:
            return

        instr, idx = self.ID_EX
        opcode = instr[0]

        if opcode == "ADD":
            _, dest, s1, s2 = instr
            val = self.cpu.registers.read(s1) + self.cpu.registers.read(s2)
            self.EX_MEM = ("ALU", dest, val, idx)

        elif opcode == "SUB":
            _, dest, s1, s2 = instr
            val = self.cpu.registers.read(s1) - self.cpu.registers.read(s2)
            self.EX_MEM = ("ALU", dest, val, idx)

        else:
            self.EX_MEM = (*instr, idx)

        print("EX:", instr)
        self.log(idx, "EX")

        self.ID_EX = None

    # ---------------- MEMORY ---------------- #
    def memory(self):
        if not self.EX_MEM:
            return

        instr = self.EX_MEM
        idx = instr[-1]

        if instr[0] == "LOAD":
            _, reg, addr, _ = instr
            val = self.cpu.memory.read(addr)
            self.MEM_WB = ("WRITE", reg, val, idx)

        elif instr[0] == "STORE":
            _, reg, addr, _ = instr
            val = self.cpu.registers.read(reg)
            self.cpu.memory.write(addr, val)
            self.MEM_WB = None

        elif instr[0] == "ALU":
            _, reg, val, _ = instr
            self.MEM_WB = ("WRITE", reg, val, idx)

        print("MEM:", instr)
        self.log(idx, "MEM")

        self.EX_MEM = None

    # ---------------- WRITE BACK ---------------- #
    def write_back(self):
        if not self.MEM_WB:
            return

        _, reg, val, idx = self.MEM_WB
        self.cpu.registers.write(reg, val)

        print("WB:", ("WRITE", reg, val))
        self.log(idx, "WB")

        self.MEM_WB = None

    # ---------------- TABLE ---------------- #
    def print_table(self):
        max_cycles = max(len(v) for v in self.pipeline_log.values())

        print("\nPipeline Timing Diagram:\n")

        header = ["Instruction"] + [f"C{i+1}" for i in range(max_cycles)]
        print(" | ".join(h.center(12) for h in header))
        print("-" * (15 * len(header)))

        for i, instr in enumerate(self.program):
            row = [f"{instr[0]} {' '.join(map(str, instr[1:]))}"]
            stages = self.pipeline_log[i]

            for j in range(max_cycles):
                if j < len(stages):
                    row.append(stages[j])
                else:
                    row.append("")

            print(" | ".join(c.center(12) for c in row))