import random, math
from metropolis import schedule

def simulated_annealing(initial_state, energy_fn, neighbor_fn, schedule_fn, T0, steps):
    state = initial_state
    energy = energy_fn(state)
    history = []

    for step in range(steps):
        T = schedule_fn(T0, step)
        new_state = neighbor_fn(state)
        new_energy = energy_fn(new_state)
        delta_E = new_energy - energy

        if delta_E < 0 or random.random() < math.exp(-delta_E / T):
            state, energy = new_state, new_energy

        history.append((step, T, energy))
    return state, energy, history