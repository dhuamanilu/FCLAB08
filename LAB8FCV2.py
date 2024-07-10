import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parámetros para el sistema de Lorenz - más extremos
a = 20.0  # Cambiado de 10.0 a 20.0
b = 50.0  # Cambiado de 28.0 a 50.0
c = 8.0   # Cambiado de 8.0 / 3.0 a 8.0

# Sistema de ecuaciones diferenciales de Lorenz
def lorenz(t, estado):
    x, y, z = estado
    dxdt = a * (y - x)
    dydt = x * (b - z) - y
    dzdt = x * y - c * z
    return [dxdt, dydt, dzdt]

# Estado inicial ajustado
estado_inicial = [0.0, 1.0, 1.05]

# Puntos de tiempo donde se computará la solución
intervalo_tiempo = (0, 100)  
tiempo_eval = np.linspace(intervalo_tiempo[0], intervalo_tiempo[1], 500000)  

# Resolver las ecuaciones diferenciales
solucion = solve_ivp(lorenz, intervalo_tiempo, estado_inicial, t_eval=tiempo_eval)

# Extraer la solución para x, y, z
x = solucion.y[0]
y = solucion.y[1]
z = solucion.y[2]

# Graficar el atractor de Lorenz
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5, color='red')  # Cambiado el color a rojo para mayor visibilidad
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Atractor de Lorenz con Parámetros Extremos")
plt.show()



