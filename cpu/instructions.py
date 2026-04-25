def execute_load(cpu, reg, addr): # Load value from memory address into register
    value = cpu.memory.read(addr)
    cpu.registers.write(reg, value)


def execute_store(cpu, reg, addr): # Store value from register into memory address
    value = cpu.registers.read(reg)
    cpu.memory.write(addr, value)


def execute_add(cpu, reg1, reg2): # Add values from two registers and store result in first register
    val1 = cpu.registers.read(reg1)
    val2 = cpu.registers.read(reg2)
    cpu.registers.write(reg1, val1 + val2)


def execute_sub(cpu, reg1, reg2): # Subtract value of second register from first register and store result in first register
    val1 = cpu.registers.read(reg1)
    val2 = cpu.registers.read(reg2) 
    cpu.registers.write(reg1, val1 - val2)