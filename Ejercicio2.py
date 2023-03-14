import numpy as np
import matplotlib.pyplot as plt
import math

E0=2
X=3
y=4
Z=5
R=6
Ti=0
Tf=6
Ts=0.0001

def Carga_estado_estable(Ti):
    return E0/Z*(float(R/Z)*math.sin(y*float(Ti))-float(X/Z)*math.cos(y*Ti))
    #return (-E0*X/y*math.pow(Z,2))*(math.sin(y*Ti))-((E0*R/y*math.pow(Z,2))*math.cos(y*Ti))

def Carga_estado_estable2(Ti):
   return (-E0*X/y*math.pow(Z,2))*(math.sin(y*Ti))-((E0*R/y*math.pow(Z,2))*math.cos(y*Ti))

t_array = np.arange(Ti, Tf, Ts)
q_array = [Carga_estado_estable(t) for t in t_array]

plt.plot(t_array, q_array)
plt.xlabel('Tiempo (s)')
plt.ylabel('Carga (C)')
plt.title('carga de estado estable')
plt.show()

t_array2 = np.arange(Ti, Tf, Ts)
q_array2 = [Carga_estado_estable2(t) for t in t_array2]
print(Carga_estado_estable(Ti))
plt.plot(t_array2, q_array2)
plt.xlabel('Tiempo (s)')
plt.ylabel('Carga (C)')
plt.title('carga de estado estable2')
plt.show()