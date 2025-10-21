#Ejemplo de aplicación (Metropolis V4.0)

#Admite argumentos en línea de comandos

from metropolis.core import simulated_annealing
import random
import argparse
import inspect

def energy_fn(x):  # Energía: pozo de potencial
    return x**2

def neighbor_fn(x):  # Perturbación aleatoria
    return x + random.uniform(-1, 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute Metropolis annealing with different scheduling types")
    parser.add_argument(
        "schedule",
        choices=["linear", "exponential", "logarithmic"],
        help="Type of scheduling to be used"
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="plotted Metropolis epochs"
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
    print("Metropolis Algorithm v4.0")
    print("(Simmulated Annealing, SA)")
    print("--------------------------")
    print("Energy Function:")
    print(inspect.getsource(energy_fn))
    print(f"Final State: {final_state:.4f}")
    print(f"Final Energy: {final_energy:.6f}")
   

    