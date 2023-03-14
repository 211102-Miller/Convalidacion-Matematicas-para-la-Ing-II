import math
import numpy as np
import matplotlib.pyplot as plt
g=9.8 #m/s^2
R=6500 #km
Rm=6.5*math.pow(10,6)
V0=(math.sqrt((2*g)*Rm))*3.6 
t0 = 0
tf = 50
dt = 0.5
def Calculo_Formula(t) :
    Formula=V0*t
   ##ingredar las fórmulas para el calculo de la distancia del cohete
    return Formula

#grafica para simulacion de salida del cohete
t_array = np.arange(t0, tf, dt)
S_array = [Calculo_Formula(t) for t in t_array]
# Graficación de la carga en función del tiempo
plt.plot(t_array, S_array) 
plt.xlabel('Tiempo (t)')
plt.ylabel('Velocidad de escape (V0)')
plt.title('Salida del cohete')
plt.show()