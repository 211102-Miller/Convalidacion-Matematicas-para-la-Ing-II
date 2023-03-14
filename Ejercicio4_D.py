import math
import numpy as np
import matplotlib.pyplot as plt
g=(6.674*10)**-11 #m/s^2
M=(7.348*10)**22
Rm=173800
V0=(math.sqrt(((2*g)*M))/Rm) 
t0 = 0
tf = 5000
dt = 10
def Calculo_Formula() :
    print(V0)
    Formula=V0
   ##ingredar las fórmulas para el calculo de la distancia del cohete
    return Formula

# Datos para la gráfica de barras
valores = Calculo_Formula()
etiquetas = ['Velocidad de escape']

# Crear la gráfica de barras
plt.bar(etiquetas, valores)

# Agregar título y etiquetas a los ejes
plt.title('Ejemplo de gráfica de barras')
plt.xlabel('')
plt.ylabel('Valores')

# Mostrar la gráfica
plt.show()