#Ejemplo de aplicación (Metropolis V4.0)

#Admite argumentos en línea de comandos

from metropolis.core import simulated_annealing
import random
import argparse

def energy_fn(x):  # Energía: cuadrado de la distancia a 0
    return x**2

def neighbor_fn(x):  # Perturbación aleatoria
    return x + random.uniform(-1, 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutar Metropolis con diferentes tipos de scheduling")
    parser.add_argument(
        "schedule",
        choices=["linear", "exponential", "logarithmic"],
        help="Tipo de scheduling a usar"
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="Graficado epochs"
    )
    args = parser.parse_args()

    initial_state = random.uniform(-10, 10)

    final_state, final_energy, history = simulated_annealing(
        initial_state,
        energy_fn,
        neighbor_fn,
        T0=100.0,
        cooling_rate=0.98,
        steps=500,
        schedule=args.schedule,
        plot=args.plot
    )

    print(f"Estado final: {final_state:.4f}")
    print(f"Energía final: {final_energy:.6f}")