class Registers:
    def __init__(self):
        # Initialize 4 general-purpose registers
        self.regs = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

    def read(self, reg):
        return self.regs.get(reg, 0)

    def write(self, reg, value):
        self.regs[reg] = value

    def __str__(self):
        return str(self.regs)