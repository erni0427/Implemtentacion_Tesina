# digestion_model/li.py

"""
Modelo del intestino grueso (LI) según Strathe et al. (2008).
Este módulo incluye:
    Pasaje no lineal (función exponencial del contenido de materia orgánica total).
    Hidrólisis de DP, EP, NAPN, ST, LD y DDF por saturación (Michaelis–Menten).
    Crecimiento microbiano a partir de carbono y nitrógeno disponibles.
    Producción de VFA, CO₂, CH₄ según coeficientes de distribución.
    Absorción inmediata de productos solubles y microbios.
Calcula la derivada de los contenidos del intestino grueso:
[DP, EP, NAPN, ST, DDF, LD, SU, FA, AA, VFA, CO2, CH4, MM]
"""

import numpy as np
from parameters import li_params, microbial_params

def michaelis_menten(S: float, vmax: float, km: float) -> float:
    return vmax * S / (km + S + 1e-9)

def pasaje_li(OM_total: float) -> float:
    """
    Tasa de pasaje del contenido del intestino grueso,
    definida como una función no lineal del total de materia orgánica.
    """
    return li_params.CLI_pa_0 * np.exp(-li_params.CLI_OM_0 * OM_total**li_params.CLI_pa_kn)

def dLI_dt(state: list[float], t: float) -> list[float]:
    """
    Derivadas para los siguientes pools en LI:
    [DP, EP, NAPN, ST, DDF, LD, SU, FA, AA, VFA, CO2, CH4, MM]
    """
    DP, EP, NAPN, ST, DDF, LD, SU, FA, AA, VFA, CO2, CH4, MM = state

    # Cálculo de OM total fermentable
    OM_total = DP + EP + NAPN + ST + DDF + LD + SU + FA + AA

    # Tasa de pasaje
    k_li = pasaje_li(OM_total)

    # Hidrólisis microbiana
    h_DP = michaelis_menten(DP, li_params.CLI_DP_hyv, li_params.CLI_DP_hyk)
    h_EP = michaelis_menten(EP, li_params.CLI_EP_hyv, li_params.CLI_EP_hyk)
    h_NAPN = michaelis_menten(NAPN, li_params.CLI_NAPN_hyv, li_params.CLI_NAPN_hyk)
    h_ST = michaelis_menten(ST, li_params.CLI_ST_hyv, li_params.CLI_ST_hyk)
    h_DDF = michaelis_menten(DDF, li_params.CLI_DDF_hyv, li_params.CLI_DDF_hyk)
    h_LD = michaelis_menten(LD, li_params.CLI_LD_hyv, li_params.CLI_LD_hyk)

    # Carbono disponible total para crecimiento microbiano
    C_source = h_ST + h_DDF + h_LD
    N_source = h_DP + h_EP + h_NAPN

    # Producción de masa microbiana
    growth = microbial_params.CMM * min(C_source, N_source)
    dMM = +growth - k_li * MM

    # C consumido por microbios (una parte queda, el resto se convierte)
    C_used = growth / microbial_params.CMM
    C_remaining = C_source - C_used

    # Productos de fermentación (basados en fracciones moleculares)
    dVFA = microbial_params.CMM_ACET_fr * C_remaining + \
           microbial_params.CMM_PROP_fr * C_remaining + \
           microbial_params.CMM_BUT_fr * C_remaining

    dCO2 = microbial_params.CMM_CO2_fr * C_remaining
    dCH4 = microbial_params.CMM_CH4_fr * C_remaining

    # Productos absorbidos (consideramos absorción inmediata)
    dSU = +h_ST - SU * k_li
    dFA = +h_LD - FA * k_li
    dAA = +h_DP + h_EP + h_NAPN - AA * k_li

    # Derivadas netas
    dDP = -h_DP - DP * k_li
    dEP = -h_EP - EP * k_li + li_params.CLI_EP_sc
    dNAPN = -h_NAPN - NAPN * k_li + li_params.CLI_NAPN_sc
    dST = -h_ST - ST * k_li
    dDDF = -h_DDF - DDF * k_li
    dLD = -h_LD - LD * k_li

    dVFA -= VFA * k_li
    dCO2 -= CO2 * k_li
    dCH4 -= CH4 * k_li

    return [dDP, dEP, dNAPN, dST, dDDF, dLD, dSU, dFA, dAA, dVFA, dCO2, dCH4, dMM]
