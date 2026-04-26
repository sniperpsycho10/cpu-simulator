from cpu.registers import Registers
from cpu.pipeline import PipelineCPU
from cpu.memory import Memory
from cpu.instructions import (
    execute_load,
    execute_store,
    execute_add,
    execute_sub
)


class CPU:
    def __init__(self):
        self.pc = 0
        self.registers = Registers()
        self.memory = Memory()
        self.program = []

    def load_program(self, program):
        self.program = program

    from cpu.pipeline import PipelineCPU

    def run(self, pipelined=False):
        if pipelined:
            pipeline_cpu = PipelineCPU(self)
            pipeline_cpu.run()
        else:
            while self.pc < len(self.program):
                instruction = self.program[self.pc]

                print(f"\nPC: {self.pc}, Instruction: {instruction}")

                self.execute(instruction)

                print("Registers:", self.registers)

                self.pc += 1

    def execute(self, instruction):
        opcode = instruction[0]

        if opcode == "LOAD":
            _, reg, addr = instruction
            execute_load(self, reg, addr)

        elif opcode == "STORE":
            _, reg, addr = instruction
            execute_store(self, reg, addr)

        elif opcode == "ADD":
            _, dest, src1, src2 = instruction
            execute_add(self, dest, src1, src2)

        elif opcode == "SUB":
            _, dest, src1, src2 = instruction
            execute_sub(self, dest, src1, src2)

        else:
            print(f"Unknown instruction: {opcode}")