# __init__.py

print("Initializing Metropolis packet..")

# API pública
#  Recursos accesibles por los clientes externos:
#   metropolis_sa.simulated_annealing
#   metropolis_sa.SCHEDULES
#   metropolis_sa.ENERGY
#   metropolis_sa.plot_history
# Nota: 
#       - main actúa como cliente externo, no cómo modulo del paquete
#       - entre módulos de paquetes debieran de usarse imports relativos para evitar ciclos!.
#       main->from metropolis_sa import...-> __init__.py -> from .core import...>
#.      ->from  metropolis_sa.schedules import ...-> __init__.py -> CICLO!!!!     

from .core import simulated_annealing

__version__ = "5.0.1"
__author__ = "Jose M. Lopez"
__email__="chema.electronica@gmail.com"

