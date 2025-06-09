
"""
Módulo que implementa la dinámica del estómago según el modelo de Strathe et al. (2008).

Incluye:
1. La función ingestion_schedule(t) que determina si hay ingestión de alimento en el tiempo t.
2. La derivada del contenido estomacal dS/dt = ingestion(t) - CSTO_pa * S
"""

import numpy as np
from typing import Callable
from digestion_model.parameters import stomach_params

def ingestion_schedule(t: float, DMI: float = None) -> float:
    """
    Retorna la tasa de ingestión (kg DM/h) en función del tiempo t (en horas),
    asumiendo que hay FFEED eventos de alimentación por día, cada uno de duración TFEED.

    Si el tiempo t cae dentro de un evento de alimentación, devuelve DMI / (FFEED * TFEED),
    de lo contrario, retorna 0.

    Parámetros:
    - t : tiempo (h)
    - DMI : ingesta total diaria de materia seca (kg DM/día). Si es None, se usa stomach_params.DMI

    Retorna:
    - tasa de ingestión en kg DM/h
    """
    if DMI is None:
        DMI = stomach_params.DMI

    T = stomach_params.TFEED
    f = stomach_params.FFEED

    t_mod = t % 24  # hora del día (0–24)
    intervalos = np.linspace(0, 24, int(f) + 1)[:-1]  # inicios de cada evento

    for inicio in intervalos:
        if inicio <= t_mod < inicio + T:
            return DMI / (f * T)  # kg DM/h

    return 0.0

def dStomach_dt(S: float, t: float) -> float:
    """
    Calcula la derivada del contenido estomacal (kg DM) en el tiempo t.

    Ecuación:
        dS/dt = ingestion_schedule(t) - CSTO_pa * S

    Donde:
    - ingestion_schedule(t): tasa de ingestión (kg/h)
    - CSTO_pa: constante de vaciado gástrico (1/h)
    - S: masa de materia seca en el estómago (kg)

    Parámetros:
    - S : masa actual en el estómago (kg)
    - t : tiempo actual (h)

    Retorna:
    - dS/dt (kg/h)
    """
    ing = ingestion_schedule(t)
    return ing - stomach_params.CSTO_pa * S

