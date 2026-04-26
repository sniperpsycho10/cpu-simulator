import sys
from cpu.core import CPU
from utils.parser import parse_program


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py programs/sample.asm")
        return

    file_path = sys.argv[1]

    cpu = CPU()

    # Preload memory
    cpu.memory.write(10, 5)
    cpu.memory.write(11, 10)

    # Parse program from file
    program = parse_program(file_path)

    cpu.load_program(program)
    cpu.run(pipelined=True)

    print("\nFinal Memory[20]:", cpu.memory.read(20))


if __name__ == "__main__":
    main()