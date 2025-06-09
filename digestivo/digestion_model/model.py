# digestion_model/model.py

"""
Modelo completo del sistema digestivo porcino, integrando todos los compartimentos:
Estómago → SI1 → SI2 → Intestino grueso (LI)
Basado en Strathe et al. (2008)
Este módulo define:
    Un vector completo de estado (con índices definidos)
    La función dSYSTEM_dt que integra todos los módulos
    Una estructura limpia y clara para futuras extensiones

Notas importantes
    El vector completo del sistema tiene 30 variables:
        1 para el estómago
        8 para SI1
        8 para SI2
        13 para LI
    Los índices se almacenan en un diccionario IDX para facilitar la lectura y evitar errores.
    Cada compartimento mantiene su lógica en su módulo respectivo.
"""

import numpy as np
from stomach import dStomach_dt
from si1 import dSI1_dt
from si2 import dSI2_dt
from li import dLI_dt

# Indices en el vector de estado
IDX = {
    'STO': 0,
    'SI1': slice(1, 9),       # 8 pools: DP, EP, NAPN, ST, LD, SU, FA, AA
    'SI2': slice(9, 17),      # 8 pools
    'LI':  slice(17, 30),     # 13 pools
}

def dSYSTEM_dt(state: list[float], t: float) -> list[float]:
    """
    Calcula la derivada del sistema digestivo completo.

    Estado:
    [STO,
     SI1: DP, EP, NAPN, ST, LD, SU, FA, AA,
     SI2: DP, ..., AA,
     LI:  DP, EP, NAPN, ST, DDF, LD, SU, FA, AA, VFA, CO2, CH4, MM]
    """
    dstate = np.zeros_like(state)

    # Compartimento estómago
    S = state[IDX['STO']]
    dstate[IDX['STO']] = dStomach_dt(S, t)

    # SI1
    si1_in = state[IDX['SI1']]
    dstate[IDX['SI1']] = dSI1_dt(si1_in, t)

    # SI2
    si2_in = state[IDX['SI2']]
    dstate[IDX['SI2']] = dSI2_dt(si2_in, t)

    # LI
    li_in = state[IDX['LI']]
    dstate[IDX['LI']] = dLI_dt(li_in, t)

    return dstate
