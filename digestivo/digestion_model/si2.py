# digestion_model/si2.py

"""
Modelo del compartimento SI2 (intestino delgado distal) según Strathe et al. (2008).
Calcula la derivada del estado: [DP, EP, NAPN, ST, LD, SU, FA, AA]
"""

from parameters import si2_params
import numpy as np

def michaelis_menten(S: float, vmax: float, km: float) -> float:
    """Cinética de saturación tipo Michaelis–Menten"""
    return vmax * S / (km + S + 1e-9)

def dSI2_dt(state: list[float], t: float) -> list[float]:
    """
    Derivadas de los pools en SI2:
    [DP, EP, NAPN, ST, LD, SU, FA, AA]
    """
    DP, EP, NAPN, ST, LD, SU, FA, AA = state

    # Hidrólisis
    hyd_DP = michaelis_menten(DP, si2_params.CSI2_DP_hyv, si2_params.CSI2_DP_hyk)
    hyd_EP = michaelis_menten(EP, si2_params.CSI2_EP_hyv, si2_params.CSI2_EP_hyk)
    hyd_NAPN = michaelis_menten(NAPN, si2_params.CSI2_NAPN_hyv, si2_params.CSI2_NAPN_hyk)
    hyd_ST = michaelis_menten(ST, si2_params.CSI2_ST_hyv, si2_params.CSI2_ST_hyk)
    hyd_LD = michaelis_menten(LD, si2_params.CSI2_LD_hyv, si2_params.CSI2_LD_hyk)

    # Absorción
    abs_SU = michaelis_menten(SU, si2_params.CSI2_SU_abv, si2_params.CSI2_SU_abk)
    abs_FA = michaelis_menten(FA, si2_params.CSI2_FA_abv, si2_params.CSI2_FA_abk)
    abs_AA = michaelis_menten(AA, si2_params.CSI2_AA_abv, si2_params.CSI2_AA_abk)

    # Pasaje
    k = si2_params.CSI2_pa

    # Derivadas
    dDP = -hyd_DP - k * DP
    dEP = -hyd_EP - k * EP
    dNAPN = -hyd_NAPN - k * NAPN
    dST = -hyd_ST - k * ST
    dLD = -hyd_LD - k * LD

    dSU = +hyd_ST - abs_SU - k * SU
    dFA = +hyd_LD - abs_FA - k * FA
    dAA = +hyd_DP + hyd_EP + hyd_NAPN - abs_AA - k * AA

    return [dDP, dEP, dNAPN, dST, dLD, dSU, dFA, dAA]
