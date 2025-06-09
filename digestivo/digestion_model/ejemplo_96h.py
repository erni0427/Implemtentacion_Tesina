# digestion_model/ejemplo.py

"""
Ejemplo completo de uso del modelo digestivo porcino (Strathe et al. 2008).
Simula el sistema completo durante 96 h y calcula digestibilidades aparentes.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from model import dSYSTEM_dt, IDX

# Tiempo de simulación
t = np.linspace(0, 96, 2000)

# Vector inicial del sistema completo (30 pools)
state0 = np.zeros(30)
state0[IDX['SI1']] = [1.0, 0.5, 0.5, 2.0, 1.5, 0.0, 0.0, 0.0]
state0[IDX['SI2']] = [0.5, 0.3, 0.3, 1.0, 0.8, 0.0, 0.0, 0.0]
state0[IDX['LI']]  = [0.3, 0.2, 0.2, 0.5, 0.8, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Integrar el sistema
result = odeint(dSYSTEM_dt, state0, t)

# Graficar curva total de VFA, MM y CH4
VFA = result[:, IDX['LI'].start + 9]
MM = result[:, IDX['LI'].start + 12]
CH4 = result[:, IDX['LI'].start + 11]

plt.figure(figsize=(10, 5))
plt.plot(t, VFA, label='Ácidos Grasos Volátiles (VFA)')
plt.plot(t, MM, label='Masa Microbiana (MM)')
plt.plot(t, CH4, label='Metano (CH4)')
plt.xlabel("Tiempo (h)")
plt.ylabel("Cantidad (mol C)")
plt.title("Producción fermentativa en intestino grueso")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Digestibilidad aparente de la proteína (ejemplo)
entrada_DP = np.trapz(result[:, IDX['SI1'].start], t)  # DP en SI1
salida_DP = np.trapz(result[:, IDX['LI'].start], t)    # DP en LI
digestibilidad_prot = 1 - (salida_DP / (entrada_DP + 1e-9))
print(f"Digestibilidad aparente de la proteína: {digestibilidad_prot:.2%}")
# digestion_model/ejemplo.py

# """
# Ejemplo completo de simulación del modelo digestivo porcino (Strathe et al. 2008).
# Incluye evaluación de producción fermentativa y digestibilidad aparente de nitrógeno.
# """

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import odeint

# from model import dSYSTEM_dt, IDX

# # Tiempo de simulación: 96 horas
# t = np.linspace(0, 96, 2000)

# # Vector de estado inicial (30 variables)
# state0 = np.zeros(30)

# # Inicializamos SI1 con nutrientes dietarios
# state0[IDX['SI1']] = [1.0, 0.0, 0.0, 2.0, 1.5, 0.0, 0.0, 0.0]
# # SI2, LI y demás inician en cero

# # Simular el sistema
# result = odeint(dSYSTEM_dt, state0, t)

# # Obtener variables de interés
# VFA = result[:, IDX['LI'].start + 9]
# CH4 = result[:, IDX['LI'].start + 11]
# MM  = result[:, IDX['LI'].start + 12]

# # Graficar fermentación
# plt.figure(figsize=(10, 5))
# plt.plot(t, VFA, label='Ácidos Grasos Volátiles (VFA)')
# plt.plot(t, MM, label='Masa Microbiana (MM)')
# plt.plot(t, CH4, label='Metano (CH₄)')
# plt.xlabel("Tiempo (h)")
# plt.ylabel("Cantidad (mol C)")
# plt.title("Producción fermentativa en intestino grueso")
# plt.grid(True)
# plt.legend()
# plt.tight_layout()
# plt.show()

# # Cálculo de digestibilidad aparente de nitrógeno
# # Entrada: solo DP dietario
# entrada_DP = np.trapz(result[:, IDX['SI1'].start + 0], t)

# # Salida: N total que queda en LI = DP + EP + NAPN
# salida_DP = np.trapz(result[:, IDX['LI'].start + 0], t)
# salida_EP = np.trapz(result[:, IDX['LI'].start + 1], t)
# salida_NAPN = np.trapz(result[:, IDX['LI'].start + 2], t)
# salida_N_total = salida_DP + salida_EP + salida_NAPN

# # Digestibilidad aparente
# digest = 1 - (salida_N_total / (entrada_DP + 1e-9))
# print(f"Digestibilidad aparente de nitrógeno: {digest:.2%}")
