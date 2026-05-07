# CPU Pipeline Simulator

A simple CPU simulator built in Python step by step from scratch.

This project started as a basic non-pipelined CPU and was gradually upgraded into a fully working 5-stage pipelined CPU with:

- Hazard Detection
- Pipeline Stalling
- Data Forwarding
- Pipeline Timing Visualization

The project was developed phase by phase to understand how real processors work internally.

---

# Features

- Instruction execution
- Register file
- Main memory simulation
- Assembly (.asm) program parsing
- 5-stage pipelined CPU
- RAW hazard detection
- Stall insertion
- Data forwarding (bypassing)
- Pipeline timing table visualization

---

# Project Structure

```text
cpu_sim/
│
├── cpu/
│   ├── core.py
│   ├── memory.py
│   ├── registers.py
│   ├── instructions.py
│   └── pipeline.py
│
├── programs/
│   └── sample.asm
│
├── utils/
│   └── parser.py
│
├── main.py
└── README.md

Phase 1 - Basic CPU Simulator

In Phase 1, a simple non-pipelined CPU was created.

The CPU could:

Load values from memory
Store values into memory
Perform ADD and SUB operations
Execute instructions one by one
Files Created / Modified

memory.py
register.py
instructions.py
core.py
main.py

Phase 2 - Assembly File Parsing

In Phase 2, hardcoded programs were removed.

Instead, programs could now be loaded from .asm files.
utils/parser.py
main.py-Modified to:
Accept .asm file from command line
Parse instructions dynamically
Program execution became fully dynamic.

Phase 3 - 5 Stage Pipeline

In Phase 3, pipelining was introduced.

The CPU was divided into 5 stages:

IF - Instruction Fetch
ID - Instruction Decode
EX - Execute
MEM - Memory Access
WB - Write Back

Modified files
pipeline.py
Created a new pipeline CPU implementation.

Pipeline registers added:
IF_ID
ID_EX
EX_MEM
MEM_WB

Phase 4 - Hazard Detection and Stalling

In Phase 4, RAW (Read After Write) hazards were handled.

Problem:
Dependent instructions were reading old register values before write-back completed.

Solution:

Detect hazards
Insert stalls (pipeline bubbles)
Freeze fetch/decode stages temporarily

Modified files
pipeline.py

Phase 5 - Data Forwarding

In Phase 5, performance was improved using forwarding (bypassing).

Instead of always stalling:

ALU results were forwarded directly
Instructions used values before register write-back

This reduced unnecessary stalls.

How to Run
Activate Virtual Environment
source cpu_sim/bin/activate

Run Program
python main.py programs/sample.asm