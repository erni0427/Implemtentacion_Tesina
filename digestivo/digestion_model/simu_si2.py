# digestion_model/simulacion_si2.py

"""
Simulación mínima del modelo de SI2 (intestino delgado distal).
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from si2 import dSI2_dt

# Tiempo de simulación (horas)
t = np.linspace(0, 24, 1000)

# Condición inicial (valores arbitrarios)
state0 = [0.5, 0.3, 0.3, 1.0, 0.8, 0.05, 0.05, 0.05]

# Ejecutar la simulación
result = odeint(dSI2_dt, state0, t)

# Etiquetas
labels = ['DP', 'EP', 'NAPN', 'ST', 'LD', 'SU', 'FA', 'AA']

# Gráfico
plt.figure(figsize=(10, 5))
for i in range(8):
    plt.plot(t, result[:, i], label=labels[i])
plt.xlabel("Tiempo (h)")
plt.ylabel("Cantidad (mol N o C)")
plt.title("Simulación de nutrientes en SI2")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
