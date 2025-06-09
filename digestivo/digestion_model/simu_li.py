# digestion_model/simulacion_li.py

"""
Simulación mínima del compartimento LI (intestino grueso) según Strathe et al. (2008).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from li import dLI_dt

# Tiempo de simulación (horas)
t = np.linspace(0, 48, 1000)

# Estado inicial [DP, EP, NAPN, ST, DDF, LD, SU, FA, AA, VFA, CO2, CH4, MM]
# Valores arbitrarios de prueba (pueden reemplazarse luego con valores reales)
state0 = [0.3, 0.2, 0.2, 0.5, 0.8, 0.3, 0.05, 0.05, 0.05, 0.0, 0.0, 0.0, 0.0]

# Integrar sistema
result = odeint(dLI_dt, state0, t)

# Etiquetas
labels = ['DP', 'EP', 'NAPN', 'ST', 'DDF', 'LD', 'SU', 'FA', 'AA', 'VFA', 'CO2', 'CH4', 'MM']

# Graficar (agrupado por tipo)
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# Sustratos (polímeros)
for i in [0, 1, 2, 3, 4, 5]:
    ax[0, 0].plot(t, result[:, i], label=labels[i])
ax[0, 0].set_title("Polímeros")
ax[0, 0].legend()
ax[0, 0].set_ylabel("mol")

# Productos solubles
for i in [6, 7, 8]:
    ax[0, 1].plot(t, result[:, i], label=labels[i])
ax[0, 1].set_title("Solubles absorbibles")
ax[0, 1].legend()

# Fermentación: VFA, CO2, CH4
for i in [9, 10, 11]:
    ax[1, 0].plot(t, result[:, i], label=labels[i])
ax[1, 0].set_title("Productos de fermentación")
ax[1, 0].legend()
ax[1, 0].set_ylabel("mol C")

# Biomasa microbiana
ax[1, 1].plot(t, result[:, 12], label='MM')
ax[1, 1].set_title("Masa microbiana")
ax[1, 1].legend()

# Estética
for i in [0, 1]:
    for j in [0, 1]:
        ax[i, j].grid(True)
        ax[i, j].set_xlabel("Tiempo (h)")

plt.tight_layout()
plt.show()
