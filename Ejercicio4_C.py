import math
import numpy as np
import matplotlib.pyplot as plt
g=9.8 #m/s^2
R=6500 #km
Rm=6.5*math.pow(10,6)
V0=(math.sqrt((2*g)*Rm))*3.6 
t0 = 0
tf = 5000
dt = 10
def Calculo_Formula() :
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