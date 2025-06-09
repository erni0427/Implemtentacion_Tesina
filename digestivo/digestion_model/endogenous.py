

"""
Funciones para calcular secreciones endógenas intestinales en función del flujo de OM,
según el modelo de Strathe et al. (2008).
Este módulo centraliza las fórmulas que antes estaban dispersas.
Este módulo tendrá funciones auxiliares que pueden ser utilizadas por SI1, SI2 y LI para calcular:
    Secreciones endógenas de proteína (EP)
    Secreciones de nitrógeno no proteico (NAPN)
    Secreciones de lípidos (LD)
"""

def secrecion_EP(flow_OM: float, f_ep: float) -> float:
    """
    Secreción de proteína endógena (EP) como fracción del flujo de OM (kg/día).
    """
    return f_ep * flow_OM

def secrecion_NAPN(flow_OM: float, f_napn: float) -> float:
    """
    Secreción de nitrógeno no proteico endógeno (NAPN).
    """
    return f_napn * flow_OM

def secrecion_LD(flow_OM: float, f_ld: float) -> float:
    """
    Secreción de lípidos endógenos como fracción del flujo de OM.
    """
    return f_ld * flow_OM
