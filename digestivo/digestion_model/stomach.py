# digestion_model/stomach.py

"""
Este módulo define las funciones del compartimento estómago:
1. ingestion_schedule(t): tasa de ingestión discontinua (kg DM/h)
2. El vaciado gástrico (cinética de primer orden) --> dStomach_dt(S, t): derivada del contenido del estómago
"""

import numpy as np
from parameters import stomach_params

def ingestion_schedule(t: float) -> float:
    """
    Retorna la tasa de ingestión (kg DM/h) según horario y frecuencia.
    """
    T = stomach_params.TFEED
    f = stomach_params.FFEED
    DMI = stomach_params.DMI

    t_mod = t % 24  # hora dentro del día
    intervalos = np.linspace(0, 24, int(f) + 1)[:-1]  # inicios de eventos

    for inicio in intervalos:
        if inicio <= t_mod < inicio + T:
            return DMI / (f * T)

    return 0.0

def dStomach_dt(S: float, t: float) -> float:
    """
    Ecuación diferencial del estómago:
    dS/dt = ingestion(t) - CSTO_pa * S
    """
    ing = ingestion_schedule(t)
    return ing - stomach_params.CSTO_pa * S
