import matplotlib.pyplot as plt
import sympy as sp
from taylor import InterpolacionTaylor
from Lagrange2 import InterpolacionLagrange
from hermite import InterpolacionHermite
from Trozos import InterpolacionATrozos

puntos = [(-2,54),(-1,4),(0,-2),(1,-6),(2,-26)]             # (x,y)
puntos_con_derivadas = [(-2,54,-92),(0,-2,0),(2,-26,-28)]   # (x,y,y')

# datos para la interpolación de taylor
x = sp.symbols('x')  
funcion = x**4 - 5*x**3 -2  
valor_x = 1  
num_derivadas = 3  
taylor = InterpolacionTaylor(funcion, valor_x, num_derivadas, x)
valores_x_grafica_taylor,valores_y_original_taylor,valores_y_taylor = taylor.run()

# datos para la interpolación de LaGrange
puntos_dados = puntos # se necesita n puntos para conseguir una función de grado n-1
lagrange = InterpolacionLagrange(puntos_dados)
puntos_x_lagrange,puntos_y_lagrange,x_grafica_lagrange,y_grafica_lagrange = lagrange.run()

# datos para la interpolacion de hermite
valores_x = [puntos_con_derivadas[0][0],puntos_con_derivadas[1][0],puntos_con_derivadas[2][0]]
valores_y = [puntos_con_derivadas[0][1],puntos_con_derivadas[1][1],puntos_con_derivadas[2][1]]
derivadas = [puntos_con_derivadas[0][2],puntos_con_derivadas[1][2],puntos_con_derivadas[2][2]]
hermite = InterpolacionHermite(valores_x, valores_y, derivadas)
valores_x_grafica_hermite,valores_y_grafica_hermite,valores_x_hermite,valores_y_hermite = hermite.run()

# datos para la interpolación A trozos
puntos_dados = puntos
trozos = InterpolacionATrozos(puntos_dados)
puntos_x_trozos,puntos_y_trozos,x_grafica_trozos,y_grafica_trozos,x_funcion_trozos,y_funcion_trozos = trozos.run()

plt.figure(figsize=(14, 7))

# grafica para taylor
plt.subplot(2, 2, 1)
plt.plot(valores_x_grafica_taylor, valores_y_taylor, label='Interpolación de Taylor', color='blue')
plt.plot(valores_x_grafica_taylor, valores_y_original_taylor, label='Función x^4 - 5x^3 -2', color='green', linestyle='--')
plt.scatter(puntos[3][0],puntos[3][1],label="Punto de aproximacion", color="red", marker="o")
plt.title('Interpolación de Taylor')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

# gráfica para LaGrange
plt.subplot(2, 2, 2)
plt.plot(x_grafica_lagrange, y_grafica_lagrange, label='Interpolación de Lagrange', color='blue')
plt.scatter(puntos_x_lagrange, puntos_y_lagrange, color='red', label='Puntos originales')
plt.title("Interpolación de Lagrange")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

# grafica para hermite
plt.subplot(2, 2, 3)  
plt.plot(valores_x_grafica_hermite, valores_y_grafica_hermite, label='Interpolación de Hermite', color='blue')
plt.scatter(valores_x_hermite, valores_y_hermite, color='red', label='Puntos originales')
plt.title('Interpolación de Hermite')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

# gráfica para a trozos
plt.subplot(2, 2, 4)
plt.plot(x_grafica_trozos, y_grafica_trozos, color='blue', label='Interpolación a trozos')
plt.plot(x_funcion_trozos, y_funcion_trozos, color='green', linestyle='--', label='Función x^4 - 5x^3 -2')
plt.scatter(puntos_x_trozos, puntos_y_trozos, color='red', label='Puntos originales')
plt.title("Interpolación a Trozos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

plt.tight_layout() # NO QUITAR, AJUSTA LOS ESPACIOS PARA EVITAR COLISIONES EN LA GRÁFICA
plt.show()

