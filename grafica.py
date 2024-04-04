import numpy as np
import matplotlib.pyplot as plt

# Define las constantes del circuito
R = 100    # resistencia en ohmios
L = 1e-3   # inductancia en henrios
C = 1e-6   # capacitancia en faradios

# Define la frecuencia de la fuente
f = 1000   # frecuencia en Hz
w = 2 * np.pi * f

# Define el rango de tiempo
t = np.linspace(0, 1e-3, 1000)

# Calcula la impedancia del circuito
Z_R = R
Z_L = w * L * 1j
Z_C = 1 / (w * C * 1j)
Z = Z_R + Z_L + Z_C

# Calcula la corriente en función del tiempo
I = np.sin(w * t) / np.abs(Z)

# Grafica la corriente en función del tiempo
plt.plot(L)
plt.plot(t, I)
plt.xlabel('Tiempo (s)')
plt.ylabel('Corriente (A)')
plt.show()

