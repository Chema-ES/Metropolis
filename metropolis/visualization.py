import matplotlib.pyplot as plt

def plot_history(history):
    steps, T, E = zip(*[(s, t, e) for s, t, e in history])
    fig, ax1 = plt.subplots()
    ax1.plot(steps, E, label="Energy", color="tab:blue")
    ax2 = ax1.twinx()
    ax2.plot(steps, T, label="Temperature", color="tab:orange", alpha=0.5)
    ax1.set_xlabel("Step")
    ax1.set_ylabel("Energy")
    ax2.set_ylabel("Temperature")
    plt.title("Simulated Annealing Convergence")
    plt.show()