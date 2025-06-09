# digestion_model/funcionamiento.py

"""
Simulación de la dinámica del contenido estomacal
usando el modelo de Strathe et al. (2008).
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Importar el modelo del estómago
from stomach import dStomach_dt

# Tiempo de simulación
t = np.linspace(0, 48, 1000)  # 48 h

# Condición inicial: masa en estómago = 0 kg
S0 = 0.0

# Resolver ODE
S = odeint(dStomach_dt, S0, t)

# Graficar
plt.plot(t, S, label='Masa en estómago')
plt.xlabel("Tiempo (h)")
plt.ylabel("Materia seca (kg)")
plt.title("Contenido estomacal según modelo de Strathe")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
