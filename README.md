# Metropolis

Una implementación pedagógica del **algoritmo de Metropolis** como núcleo del método de **Simulated Annealing**.

- Soporte para **4 paisajes energéticos** monodimensionales:

    - square
    - cube
    - abs
    - bimodal

- Soporte **3 schedules** de enfriamiento:

    - lineal
    - logarítmico
    - exponencial

- **Tracking gráfico** de la evolución energética durante el enfriamiento

## Instalación

1. En tu entorno de Anaconda (u otro entorno virtual):

```bash
pip install -e .
```
Esto instala el paquete localmente en modo editable.

2. Si se prefiere usar dependencias explícitas:

```bash
pip install -r requirements.txt
```

3. Como paquete PIP

```bash
pip install metropolis-SA==5.0.1
```

## Estructura Metropolis V5.0.0

```text
Metropolis-SA/
├── README.md
├── LICENSE
├── requirements.txt
├── metropolis/
│   ├── __init__.py      # inicialización paquete
│   ├── core.py          # núcleo del algoritmo
│   ├── main.py          # main metropolis
│   ├── schedule.py      # funciones de temperatura (v2+)
│   ├── energies.py      # funciones de temperatura (v5+)
│   └── visualization.py # para plots de convergencia (v3+)
├── test/
│   └── anneal.py
└── tests/
``` 

## Estructura Metropolis V5.0.1

```text
Metropolis-SA/
├── README.md
├── LICENSE
├── requirements.txt
├── src/
    ├── main.py             # main metropolis
    ├──metropolis_sa 
        ├── __init__.py      # inicialización paquete
        ├── core.py          # núcleo del algoritmo
        ├── schedule.py      # funciones de temperatura (v2+)
│       ├── energies.py      # funciones de temperatura (v5+)
│       └── visualization.py # para plots de convergencia (v3+)
├── test/
│   └── anneal.py
└── doc/
``` 

## Ejecución

1. **Como módulo ejecutable (sin instalación previa)**

```
#from packet root
usage: python -m metropolis.main [-h] [--schedule {linear,exponential,logarithmic}] [--plot] {square,abs,cube,bimodal}

Execute Metropolis annealing with different energy landscapes and scheduling types

positional arguments:
  {square,abs,cube,bimodal}
                        Energy landscape

options:
  -h, --help            show this help message and exit
  --schedule {linear,exponential,logarithmic}
                        Type of scheduling to be used (default: exponential)
  --plot                Plotted Metropolis epochs

```

Ejemplos:

```bash
python -m metropolis.main square --plot
python -m metropolis.main bimodal --schedule exponential --plot
python -m metropolis.main bimodal --schedule linear
```

### Versión >=5.0.1

Desde raiz del paquete usar /src/main

```bash
python -m main square --plot
python -m main bimodal --schedule exponential --plot
python -m main bimodal --schedule linear
```

2. **Instalándolo como paquete PIP**

Instalando el paquete desde PyPI, se habilita el comando de consola con entry point **metropolis-run**.

```bash
pip install metropolis-SA==5.0.1
metropolis-SA 
```
   
Ejemplos:

```bash
metropolis-SA -h 
metropolis-SA  bimodal --schedule exponential --plot
metropolis-SA quare --schedule linear --plot
```

## Historial

V1.0.0
Motor Monte Carlo básico
Ejemplo de uso

V2.0.0
Incorpora varios schedules  de enfriamiento

V3.0.0
- Añadido Módulo `visualization.py` para graficar convergencia.
- Corregido bug en orden de parámetros de llamada a la función scheduling
- Se evitan energías negativas
- Otros cambios menores.

V4.0.0
- Añadido soporte línea de comandos.

V5.0.0
- Versión final estable
- Posibilidad de indicar función paisaje-energético
- Integrado un main al paquete
- Añadido como paquete PIP 
- Salida en inglés

V5.0.1
- Reorganización de módulos
- cambios menores

## Creación de releases
### Flujo recomendado
git add .
git commit -m "Prepare release vx.x.x"
git push

git tag -a v1x.x.x -m "Release vx.x.x"
git push origin vx.x.x

gh release create vx.x