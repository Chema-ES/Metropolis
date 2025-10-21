#Módulo de visualización (Metropolis V3.0)

import matplotlib.pyplot as plt

def plot_history(history):
    """Dibuja la evolución de la energía durante el annealing."""
    plt.figure(figsize=(8, 4))
    plt.plot(history, label="Energía", linewidth=1.5)
    plt.xlabel("Iteración")
    plt.ylabel("Energía")
    plt.title("Evolución de la energía (Metropolis Annealing)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()