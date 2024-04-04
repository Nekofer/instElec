import numpy as np

# Define las constantes del circuito
R = 100   # resistencia en ohmios
L = 1e-3  # inductancia en henrios
C = 1e-6  # capacitancia en faradios
f = 1000  # frecuencia en Hz

# Calcula la impedancia total del circuito
w = 2 * np.pi * f
Z_R = R
Z_L = w * L * 1j
Z_C = 1 / (w * C * 1j)
Z_total = Z_R + Z_L + Z_C

# Calcula la corriente y su desfase
V = 220  # tensión en voltios
I = np.abs(V / Z_total)
phi = np.angle(Z_total)

# Calcula las potencias
P = V * I * np.cos(phi)
Q = V * I * np.sin(phi)
S = V * I
PF = np.cos(phi)

# Imprime los resultados
print("Impedancia total: {:.2f} Ohm".format(np.abs(Z_total)))
print("Corriente: {:.2f} A, Desfase: {:.2f} rad".format(I, phi))
print("Potencia activa: {:.2f} W".format(P))
print("Potencia reactiva: {:.2f} VAR".format(Q))
print("Potencia aparente: {:.2f} VA".format(S))
print("Factor de potencia: {:.2f}".format(PF))
