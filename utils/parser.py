def parse_program(file_path):
    program = []

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            parts = line.split()

            opcode = parts[0]

            if opcode == "LOAD" or opcode == "STORE":
                reg = parts[1]
                addr = int(parts[2])
                program.append((opcode, reg, addr))

            elif opcode == "ADD" or opcode == "SUB":
                dest = parts[1]
                src1 = parts[2]
                src2 = parts[3]
                program.append((opcode, dest, src1, src2))

            else:
                raise ValueError(f"Unknown instruction: {opcode}")

    return program