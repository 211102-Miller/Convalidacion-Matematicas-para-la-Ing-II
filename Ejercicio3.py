import numpy as np
import matplotlib.pyplot as plt
import math
# Tiempo inicial y final
t0 = 0
tf = 9
dt = 0.5

# Definición de la ecuación diferencial
def q_prime_prime(t):
    return 30-1.633*math.pow((t-4.286),2)

# Solución numérica de la ecuación diferencial
t_array = np.arange(t0, tf, dt)
q_array = [q_prime_prime(t) for t in t_array]

# Graficación de la carga en función del tiempo
plt.plot(t_array,q_array)
plt.xlabel('Tiempo (s)')
plt.ylabel('Fuerza (F)')
plt.title('Carga en función del tiempo')
plt.show()