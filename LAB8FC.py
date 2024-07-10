import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parámetros para el sistema de Lorenz
a = 10.0
b = 28.0
c = 8.0 / 3.0

# Sistema de ecuaciones diferenciales de Lorenz
def lorenz(t, estado):
    x, y, z = estado
    dxdt = a * (y - x)
    dydt = x * (b - z) - y
    dzdt = x * y - c * z
    return [dxdt, dydt, dzdt]

# Estado inicial
estado_inicial = [1.0, 1.0, 1.0]

# Puntos de tiempo dondese computará la solución
intervalo_tiempo = (0, 50)
tiempo_eval = np.linspace(intervalo_tiempo[0], intervalo_tiempo[1], 1000000)

# Resolver las ecuaciones diferenciales
solucion = solve_ivp(lorenz, intervalo_tiempo, estado_inicial, t_eval=tiempo_eval)

# Extraer la solución para x, y, z
x = solucion.y[0]
y = solucion.y[1]
z = solucion.y[2]

# Graficar el atractor de Lorenz
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Atractor de Lorenz")
plt.show()
