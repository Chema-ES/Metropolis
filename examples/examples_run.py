from metropolis.core import simulated_annealing
import random

def energy_fn(x): return x**2

def neighbor_fn(x): return x + random.uniform(-1, 1)

best_state, best_energy = simulated_annealing(
    initial_state=5.0, energy_fn=energy_fn,
    neighbor_fn=neighbor_fn, T0=10, cooling_rate=0.99, steps=1000
)

print("Best state:", best_state, "Energy:", best_energy)