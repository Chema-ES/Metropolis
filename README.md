# Metropolis

Implementación del **algoritmo de Metropolis** como núcleo del método de **Simulated Annealing**


## Instalación

En tu entorno de Anaconda (u otro entorno virtual):

```bash
pip install -e .
```
Esto instala el paquete localmente en modo editable.

Si se prefiere usar dependencias explícitas:

```bash
pip install -r requirements.txt
```

## Estructura Metropolis V1.0

```bash
Metropolis/
├── metropolis/
│   ├── core.py
│ 
├── examples/
│   └── example_run.py
├── README.md
├── LICENSE
└── requirements.txt
```


## Ejecución

Ejecuta desde la raíz del proyecto:

```bash
python -m examples.example_run
```

## Historial

V1.0
Motor Monte Carlo básico
Ejemplo de uso

V2.0
Incorpora varios schedules  de enfriamiento

V3.0
- Añadido Módulo `visualization.py` para graficar convergencia.
- Corregido bug en orden de parámetros de llamada a la función scheduling
- Se evitan energías negativas
- Otros cambios menores.