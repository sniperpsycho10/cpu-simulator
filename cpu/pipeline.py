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

    def is_done(self):
        return (
            self.pc >= len(self.program)
            and self.IF_ID is None
            and self.ID_EX is None
            and self.EX_MEM is None
            and self.MEM_WB is None
        )

    def run(self):
        while not self.is_done():
            self.cycle += 1
            print(f"\nCycle {self.cycle}")

            self.write_back()
            self.memory()
            self.execute()
            self.decode()
            self.fetch()

    def fetch(self):
        if self.pc < len(self.program):
            instr = self.program[self.pc]
            self.IF_ID = instr
            print("IF:", instr)
            self.pc += 1

    def decode(self):
        if self.IF_ID:
            self.ID_EX = self.IF_ID
            print("ID:", self.ID_EX)
            self.IF_ID = None

    def execute(self):
        if self.ID_EX:
            instr = self.ID_EX
            opcode = instr[0]

            if opcode == "ADD":
                _, dest, src1, src2 = instr
                val = self.cpu.registers.read(src1) + self.cpu.registers.read(src2)
                self.EX_MEM = ("ALU", dest, val)

            elif opcode == "SUB":
                _, dest, src1, src2 = instr
                val = self.cpu.registers.read(src1) - self.cpu.registers.read(src2)
                self.EX_MEM = ("ALU", dest, val)

            else:
                self.EX_MEM = instr

            print("EX:", instr)
            self.ID_EX = None

    def memory(self):
        if self.EX_MEM:
            instr = self.EX_MEM

            if instr[0] == "LOAD":
                _, reg, addr = instr
                val = self.cpu.memory.read(addr)
                self.MEM_WB = ("WRITE", reg, val)

            elif instr[0] == "STORE":
                _, reg, addr = instr
                val = self.cpu.registers.read(reg)
                self.cpu.memory.write(addr, val)
                self.MEM_WB = None

            elif instr[0] == "ALU":
                _, dest, val = instr
                self.MEM_WB = ("WRITE", dest, val)

            print("MEM:", instr)
            self.EX_MEM = None

    def write_back(self):
        if self.MEM_WB:
            _, reg, val = self.MEM_WB
            self.cpu.registers.write(reg, val)
            print("WB:", self.MEM_WB)
            self.MEM_WB = None