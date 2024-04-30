import matplotlib.pyplot as plt

# Data
n_values = [100, 250, 500, 1000]
p_values = [2, 4, 8]
speedup_values = {
    100: [3.98607, 15.79499, 66.63112],
    250: [3.989606, 16.30609, 64.96939],
    500: [4.40032, 17.595798, 69.96692],
    1000: [3.99225, 16.01525, 63.95112]
}
colors = ['r', 'g', 'b', 'm']
markers = ['o', 's', '^', 'd']  # markers for each n value

# Plotting
plt.figure(figsize=(10, 6))

for i, n in enumerate(n_values):
    plt.plot(p_values, speedup_values[n], marker=markers[i], linestyle='-', color=colors[i], label=f"n={n}")

plt.xlabel("Number of Processors (P)")
plt.ylabel("Speedup (S)")
plt.title("Speedup vs. Number of Processors")
plt.xticks(p_values)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
