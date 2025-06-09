"""
Simulación mínima del modelo de SI2 (intestino delgado distal).
"""
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from si1 import dSI1_dt

# Tiempo de simulación
t = np.linspace(0, 24, 1000)

# Condición inicial (valores arbitrarios de masa o concentración)
state0 = [1.0, 0.5, 0.5, 2.0, 1.5, 0.1, 0.1, 0.1]

# Integrar el sistema de ecuaciones diferenciales
result = odeint(dSI1_dt, state0, t)

# Etiquetas para cada curva
labels = ['DP', 'EP', 'NAPN', 'ST', 'LD', 'SU', 'FA', 'AA']

# Graficar resultados
plt.figure(figsize=(10, 5))
for i in range(8):
    plt.plot(t, result[:, i], label=labels[i])
plt.xlabel("Tiempo (h)")
plt.ylabel("Cantidad (mol N o C)")
plt.title("Dinámica de los nutrientes en SI1")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
