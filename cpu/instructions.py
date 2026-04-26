def execute_load(cpu, reg, addr): # Load value from memory address into register
    value = cpu.memory.read(addr)
    cpu.registers.write(reg, value)


def execute_store(cpu, reg, addr): # Store value from register into memory address
    value = cpu.registers.read(reg)
    cpu.memory.write(addr, value)


def execute_add(cpu, dest, src1, src2):
    val1 = cpu.registers.read(src1)
    val2 = cpu.registers.read(src2)
    cpu.registers.write(dest, val1 + val2)


def execute_sub(cpu, dest, src1, src2):
    val1 = cpu.registers.read(src1)
    val2 = cpu.registers.read(src2)
    cpu.registers.write(dest, val1 - val2)