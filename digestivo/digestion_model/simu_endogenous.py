# digestion_model/simulacion_endogenous.py

"""
Simulación mínima de secreciones endógenas en función del flujo de OM.
"""

import numpy as np
import matplotlib.pyplot as plt

from endogenous import secrecion_EP,secrecion_NAPN,secrecion_LD

# Vector de flujos de OM (kg/día)
flow_OM = np.linspace(0, 2, 200)

# Constantes de secreción (valores reales desde parameters.py)
f_EP = 0.07 + 0.077    # pancreática + biliar
f_NAPN = 0.03 + 0.042
f_LD = 1.25

# Cálculo
EP = secrecion_EP(flow_OM, f_EP)
NAPN = secrecion_NAPN(flow_OM, f_NAPN)
LD = secrecion_LD(flow_OM, f_LD)

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(flow_OM, EP, label='EP (mol N/d)')
plt.plot(flow_OM, NAPN, label='NAPN (mol N/d)')
plt.plot(flow_OM, LD, label='LD (mol C/d)')
plt.xlabel("Flujo de OM (kg/día)")
plt.ylabel("Secreción endógena")
plt.title("Secreciones endógenas en función del flujo de OM")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
