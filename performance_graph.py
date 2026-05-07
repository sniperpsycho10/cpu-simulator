import matplotlib.pyplot as plt


# ---------------- PHASE 4 VALUES ---------------- #
phase4_cycles = 10
phase4_cpi = 2.5
phase4_stalls = 3

# ---------------- PHASE 5 VALUES ---------------- #
phase5_cycles = 8
phase5_cpi = 2.0
phase5_stalls = 1

labels = ["Phase 4", "Phase 5"]


# ---------------- TOTAL CYCLES GRAPH ---------------- #
plt.figure(figsize=(5, 4))

plt.bar(labels, [phase4_cycles, phase5_cycles])

plt.title("Total Cycles Comparison")

plt.ylabel("Cycles")

plt.show()


# ---------------- CPI GRAPH ---------------- #
plt.figure(figsize=(5, 4))

plt.bar(labels, [phase4_cpi, phase5_cpi])

plt.title("CPI Comparison")

plt.ylabel("CPI")

plt.show()


# ---------------- STALL COUNT GRAPH ---------------- #
plt.figure(figsize=(5, 4))

plt.bar(labels, [phase4_stalls, phase5_stalls])

plt.title("Stall Count Comparison")

plt.ylabel("Stalls")

plt.show()