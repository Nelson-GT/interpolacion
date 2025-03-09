# interpolacion

## Enunciado:
En la ciudad de Estocolmo se hicieron investigaciones meteorológicas, donde se buscaba encontrar las temperaturas y procesar la información para analizar el cambio climático de la región, en las investigaciones dadas se evaluaron las temperaturas en un periodo de 24 horas, con 4.8 horas entre análisis, los datos obtenidos fueron: 

- ( -2, 54)

- ( -1, 4)

- ( 0, -2)

- (1, -6)

- ( 2, -26)

Se determinó que la temperatura tenía un comportamiento similar a la expresión matemática:  t = x^4 - 5x^3 - 2 . Por último, se intuye que los valores de las funciones derivadas para -2, 0 y 2 son -92, 0 y -28 respectivamente.  Conociendo estos datos el equipo de investigadore desea realizar una interpolación para estos datos por 4 diferentes métodos, con la finalidad de comparar los resultados, estos métodos son: Taylor, Lagrange, Hermite, y Polinómica a trozos (Interpolador por splines).

Además, para la interpolación de Taylor, se desea aproximar al punto x = 1, con un máximo de 3 derivadas.