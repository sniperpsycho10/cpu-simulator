from cpu.core import CPU


def main():
    cpu = CPU()

    # Preload memory (example values)
    cpu.memory.write(10, 5)
    cpu.memory.write(11, 10)

    # Program (hardcoded for Phase 1)
    program = [
        ("LOAD", "R1", 10),   # 5
        ("LOAD", "R2", 11),   # 10
        ("ADD", "R3", "R1", "R2"),   # 15
        ("SUB", "R2", "R3", "R1"),   # 15 - 5 = 10
        ("SUB", "R1", "R2", "R3"),   # 10 - 15 = -5
        ("STORE", "R1", 20)
    ]

    cpu.load_program(program)
    cpu.run()

    print("\nFinal Memory[20]:", cpu.memory.read(20))


if __name__ == "__main__":
    main()