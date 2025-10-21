#Ejemplo de aplicación (Metropolis V3.0)

#Paisaje energético: pozo de potencial con mínimo en x=0)

from metropolis.core import simulated_annealing
import random

def energy_fn(x):  # Energía: cuadrado de la distancia a 0
    return x**2

def neighbor_fn(x):  # Perturbación aleatoria
    return x + random.uniform(-1, 1)

if __name__ == "__main__":
    initial_state = random.uniform(-10, 10)

    # Parámetros configurables
    schedule = "exponential"   # "linear", "exponential", "logarithmic"
    plot = True                # activa visualización

    final_state, final_energy, history = simulated_annealing(
        initial_state,
        energy_fn,
        neighbor_fn,
        T0=100.0,
        cooling_rate=0.99,
        steps=500,
        schedule=schedule,
        plot=plot
    )

    print(f"Estado final: {final_state:.4f}")
    print(f"Energía final: {final_energy:.6f}")