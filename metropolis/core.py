from metropolis.visualization import plot_history
import random

def simulated_annealing(initial_state, energy_fn, neighbor_fn,
                        T0=10.0, cooling_rate=0.99, steps=1000,
                        plot=True):
    """
    Algoritmo de Metropolis para Simulated Annealing.
    """
    state = initial_state
    energy = energy_fn(state)
    history = [energy]
    T = T0

    for step in range(steps):
        candidate = neighbor_fn(state)
        candidate_energy = energy_fn(candidate)
        delta = candidate_energy - energy

        if delta < 0 or random.random() < min(1, pow(2.71828, -delta/T)):
            state, energy = candidate, candidate_energy

        history.append(energy)
        T *= cooling_rate

    if plot:
        plot_history(history)

    return state, energy, history