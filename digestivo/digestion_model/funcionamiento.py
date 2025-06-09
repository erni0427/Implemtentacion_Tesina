from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from stomach import dStomach_dt

t = np.linspace(0, 24, 1000)        # tiempo en horas
S0 = 0.0                            # masa inicial en el estómago (kg)
S = odeint(dStomach_dt, S0, t)      # integración

plt.plot(t, S)
plt.xlabel("Tiempo (h)")
plt.ylabel("Masa en estómago (kg)")
plt.title("Dinámica del contenido estomacal")
plt.show()
