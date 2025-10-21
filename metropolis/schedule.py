import math

def exponential(T0, rate, step):
    """Enfriamiento exponencial: T = T0 * rate**step"""
    return T0 * (rate ** step)

def linear(T0, rate, step):
    """Enfriamiento lineal: T = T0 - rate*step"""
    return max(T0 - rate * step, 1e-6)

def logarithmic(T0, rate, step):
    """Enfriamiento logarítmico: T = T0 / log(2 + step)"""
    return T0 / math.log(2 + step)

SCHEDULES = {
    "linear": linear,
    "exponential": exponential,
    "logarithmic": logarithmic,
}