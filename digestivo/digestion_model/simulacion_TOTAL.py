# digestion_model/simulacion_total.py

"""
Simulación completa del sistema digestivo porcino basado en el modelo de Strathe et al. (2008).
Incluye estómago, intestino delgado (SI1, SI2) e intestino grueso (LI).
Este archivo:
    Define el vector completo de estado inicial.
    Simula durante 96 h (como en Strathe et al. 2008).
    Integra con scipy.integrate.odeint usando la función dSYSTEM_dt.
    Genera gráficos agrupados por compartimento (STO, SI1, SI2, LI).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from model import dSYSTEM_dt, IDX

# Tiempo de simulación (96 h = 4 días)
t = np.linspace(0, 96, 2000)

# Vector de estado inicial (30 variables)
# [STO, SI1 (8), SI2 (8), LI (13)]
state0 = np.zeros(30)

# Supuestos iniciales (valores razonables para ejemplo)
state0[IDX['STO']] = 0.0
state0[IDX['SI1']] = [1.0, 0.5, 0.5, 2.0, 1.5, 0.1, 0.1, 0.1]
state0[IDX['SI2']] = [0.5, 0.3, 0.3, 1.0, 0.8, 0.05, 0.05, 0.05]
state0[IDX['LI']]  = [0.3, 0.2, 0.2, 0.5, 0.8, 0.3, 0.05, 0.05, 0.05, 0.0, 0.0, 0.0, 0.0]

# Simular
result = odeint(dSYSTEM_dt, state0, t)

# Etiquetas por compartimento
labels = {
    'STO': ['Estómago'],
    'SI1': ['DP', 'EP', 'NAPN', 'ST', 'LD', 'SU', 'FA', 'AA'],
    'SI2': ['DP', 'EP', 'NAPN', 'ST', 'LD', 'SU', 'FA', 'AA'],
    'LI':  ['DP', 'EP', 'NAPN', 'ST', 'DDF', 'LD', 'SU', 'FA', 'AA', 'VFA', 'CO2', 'CH4', 'MM']
}

# Función para graficar un compartimento
def plot_section(ax, t, data, indices, names, title):
    for i, name in zip(indices, names):
        ax.plot(t, data[:, i], label=name)
    ax.set_title(title)
    ax.set_xlabel("Tiempo (h)")
    ax.set_ylabel("Cantidad")
    ax.legend()
    ax.grid(True)

# Crear subplots
fig, ax = plt.subplots(2, 2, figsize=(14, 8))

plot_section(ax[0, 0], t, result, [IDX['STO']], labels['STO'], "Estómago")
plot_section(ax[0, 1], t, result, range(*IDX['SI1'].indices(30)), labels['SI1'], "SI1")
plot_section(ax[1, 0], t, result, range(*IDX['SI2'].indices(30)), labels['SI2'], "SI2")
plot_section(ax[1, 1], t, result, range(*IDX['LI'].indices(30)), labels['LI'], "Intestino grueso (LI)")

plt.tight_layout()
plt.show()
