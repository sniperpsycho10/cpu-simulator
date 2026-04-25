class Memory:
    def __init__(self, size=256):
        self.mem = [0] * size

    def read(self, addr):
        return self.mem[addr]

    def write(self, addr, value):
        self.mem[addr] = value

    def __str__(self):
        return str(self.mem[:20])  # show first 20 for debugging