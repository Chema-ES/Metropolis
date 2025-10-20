import math
import random

def metropolis_step(current_state, current_energy, neighbor_fn, energy_fn, T):
    """Ejecuta un paso del algoritmo de Metropolis."""
    new_state = neighbor_fn(current_state)
    new_energy = energy_fn(new_state)
    delta_E = new_energy - current_energy

    if delta_E < 0 or random.random() < math.exp(-delta_E / T):
        return new_state, new_energy
    return current_state, current_energy

def simulated_annealing(initial_state, energy_fn, neighbor_fn, T0, cooling_rate, steps):
    state = initial_state
    energy = energy_fn(state)
    T = T0

    for _ in range(steps):
        state, energy = metropolis_step(state, energy, neighbor_fn, energy_fn, T)
        T *= cooling_rate

    return state, energy