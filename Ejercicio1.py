import numpy as np
import matplotlib.pyplot as plt
import math

# Datos del circuito
L = 0.25  # Inductancia (H)
R = 10  # Resistencia (ohm)
C = 0.001  # Capacitancia (F)
E = 0  # Fuerza electromotriz (V)
q0 = 0.001 
c2=q0/3
# Tiempo inicial y final
t0 = 0
tf = 3
dt = 0.0001

# Definición de la ecuación diferencial
def q_prime_prime(t):
    return q0*math.sqrt(10)/3*math.exp(-20*float(t))*(math.sin(60*float(t)+1.249))



# Solución numérica de la ecuación diferencial
t_array = np.arange(t0, tf, dt)
q_array = [q_prime_prime(t) for t in t_array]

# Graficación de la carga en función del tiempo
plt.plot(t_array, q_array)
plt.xlabel('Tiempo (s)')
plt.ylabel('Carga (C)')
plt.title('Carga en función del tiempo')
plt.show()