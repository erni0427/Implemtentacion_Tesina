# digestion_model/si1.py

"""
Modelo del compartimento SI1 (intestino delgado proximal) del sistema digestivo porcino.
Basado en Strathe et al. (2008).
Este módulo debe:
    Importar parámetros desde digestion_model.parameters.
    Calcular pasaje hacia SI2.
    Calcular hidrólisis enzimática de polímeros: DP, EP, NAPN, ST, LD (Michaelis–Menten).
    Calcular absorción de productos solubles: AA, SU, FA (también Michaelis–Menten).
    Incluir secreciones endógenas: EP pancreático/biliar, NAPN, LD.
Supone un vector de estados de entrada del tipo:
[DP, EP, NAPN, ST, LD, SU, FA, AA]
Y devuelve su derivada:
[dDP/dt, dEP/dt, ..., dAA/dt]

Este módulo calcula la derivada de cada componente del vector de estado de SI1:
[DP, EP, NAPN, ST, LD, SU, FA, AA]
"""

from parameters import si1_params
import numpy as np

def michaelis_menten(S: float, vmax: float, km: float) -> float:
    """Cinética de saturación tipo Michaelis–Menten"""
    return vmax * S / (km + S + 1e-9)

def dSI1_dt(state: list[float], t: float) -> list[float]:
    """
    Calcula las derivadas del contenido en SI1 para los siguientes pools:
    DP, EP, NAPN, ST, LD, SU, FA, AA

    Ecuaciones:
    - Hidrólisis: dX/dt -= MM(X)
    - Productos: dP/dt += MM(X)
    - Absorción: dP/dt -= MM(P)
    - Secreciones: entradas constantes al sistema

    Retorna:
    - derivadas [dDP, dEP, dNAPN, dST, dLD, dSU, dFA, dAA]
    """
    # Desempaquetar estado
    DP, EP, NAPN, ST, LD, SU, FA, AA = state

    # Hidrólisis de polímeros
    hyd_DP = michaelis_menten(DP, si1_params.CSI1_DP_hyv, si1_params.CSI1_DP_hyk)
    hyd_EP = michaelis_menten(EP, si1_params.CSI1_EP_hyv, si1_params.CSI1_EP_hyk)
    hyd_NAPN = michaelis_menten(NAPN, si1_params.CSI1_NAPN_hyv, si1_params.CSI1_NAPN_hyk)
    hyd_ST = michaelis_menten(ST, si1_params.CSI1_ST_hyv, si1_params.CSI1_ST_hyk)
    hyd_LD = michaelis_menten(LD, si1_params.CSI1_LD_hyv, si1_params.CSI1_LD_hyk)

    # Absorción de productos solubles
    abs_SU = michaelis_menten(SU, si1_params.CSI1_SU_abv, si1_params.CSI1_SU_abk)
    abs_FA = michaelis_menten(FA, si1_params.CSI1_FA_abv, si1_params.CSI1_FA_abk)
    abs_AA = michaelis_menten(AA, si1_params.CSI1_AA_abv, si1_params.CSI1_AA_abk)

    # Secreciones endógenas
    sc_EP = si1_params.CSI1_EPp_sc + si1_params.CSI1_EPb_sc
    sc_NAPN = si1_params.CSI1_NAPNp_sc + si1_params.CSI1_NAPNb_sc
    sc_LD = si1_params.CSI1_LD_sc

    # Tasa de pasaje a SI2
    pasaje = si1_params.CSI1_pa

    # Derivadas
    dDP = -hyd_DP - pasaje * DP
    dEP = -hyd_EP + sc_EP - pasaje * EP
    dNAPN = -hyd_NAPN + sc_NAPN - pasaje * NAPN
    dST = -hyd_ST - pasaje * ST
    dLD = -hyd_LD + sc_LD - pasaje * LD

    dSU = +hyd_ST - abs_SU - pasaje * SU
    dFA = +hyd_LD - abs_FA - pasaje * FA
    dAA = +hyd_DP + hyd_EP + hyd_NAPN - abs_AA - pasaje * AA

    return [dDP, dEP, dNAPN, dST, dLD, dSU, dFA, dAA]
