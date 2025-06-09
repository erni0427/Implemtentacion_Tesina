# digestion_model/test_digestibilidad.py

"""
Pruebas fisiológicas del modelo digestivo porcino basado en Strathe et al. (2008).
Se validan digestibilidades, producción microbiana, CH4 y estabilidad.
"""

import numpy as np
from scipy.integrate import odeint

from model import dSYSTEM_dt, IDX

def simulate_96h():
    """Simula 96h del sistema completo con condiciones iniciales razonables"""
    t = np.linspace(0, 96, 2000)
    state0 = np.zeros(30)
    state0[IDX['SI1']] = [1.0, 0.5, 0.5, 2.0, 1.5, 0, 0, 0]
    state0[IDX['SI2']] = [0.5, 0.3, 0.3, 1.0, 0.8, 0, 0, 0]
    state0[IDX['LI']] = [0.3, 0.2, 0.2, 0.5, 0.8, 0.3, 0, 0, 0, 0, 0, 0, 0]

    result = odeint(dSYSTEM_dt, state0, t)
    return t, result

def test_digestibilidad_proteica():
    t, result = simulate_96h()
    entrada_DP = np.trapz(result[:, IDX['SI1'].start], t)  # DP en SI1
    salida_DP = np.trapz(result[:, IDX['LI'].start], t)    # DP en LI
    digest = 1 - (salida_DP / (entrada_DP + 1e-9))
    assert 0.70 < digest <= 1.00, f"Digestibilidad fuera de rango: {digest:.2%}"

def test_produccion_microbiana():
    t, result = simulate_96h()
    MM = result[:, IDX['LI'].start + 12]
    assert MM[-1] > 0.05, f"Masa microbiana final baja: {MM[-1]:.3f}"

def test_CH4_generado():
    t, result = simulate_96h()
    CH4 = result[:, IDX['LI'].start + 11]
    CH4_total = np.trapz(CH4, t)
    assert CH4_total >= 0, f"Producción negativa de CH4: {CH4_total:.3f}"

def test_estabilidad_final():
    t, result = simulate_96h()
    final = result[-1, :]
    prev = result[-10, :]
    dif = np.abs(final - prev)
    assert np.all(dif < 0.01), "Sistema no converge al final del período"
