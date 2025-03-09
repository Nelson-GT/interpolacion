# Interpolación
## Pasos para iniciar el proyecto.
#### Paso 1:
Primeramente, debe crear un entorno virtual de python en su equipo, para esto, ejecute el siguiente codigo en su consola, en la ubicación que desee.

`virtualenv -p python env`

> [!WARNING]
> En caso de no tener descargado la libreria virtualenv (Se puede comprobar buscando su nombre si se escribe `pip list`), debe descargarlo escribiendo el siguiente comando en su consola: `pip install virtualenv`

#### Paso 2:
Luego, entrará a su entorno virtual y clonará el repositorio dentro del mismo, escribiendo el siguiente comando en la git Bash:
`git clone https://github.com/Nelson-GT/interpolacion.git`

#### Paso 3:
Ahora, procederá a activarlo, escribiendo en la consola, con la ubicación de su entorno el siguiente comando:
`env\Scripts\activate`

#### Paso 4:
Seguidamente, procederá a instalar las dependencias necesarias, escribiendo en la consola el siguiente comando: 
`pip install -r requirements.txt`

#### Paso 5:
Con esto, ya podrá ejecutar el archivo <b>main.py</b>, el cual es el principal del proyecto, este abrirá una nueva ventana donde se podrá apreciar las 4 gráficas de las interpolaciones, y por consola podrá ver los polinomio de cada tipo de interpolación. Si desea ejecutar el archivo python desde su consola, escriba en ella lo siguiente:
`python main.py`


## Enunciado:
En la ciudad de Estocolmo se hicieron investigaciones meteorológicas, donde se buscaba encontrar las temperaturas y procesar la información para analizar el cambio climático de la región, en las investigaciones dadas se evaluaron las temperaturas en un periodo de 24 horas, con 4.8 horas entre análisis, los datos obtenidos fueron: 
<b>
- ( -2, 54)

- ( -1, 4)

- ( 0, -2)

- (1, -6)

- ( 2, -26)
</b>
Se determinó que la temperatura tenía un comportamiento similar a la expresión matemática:  <b>t = x^4 - 5x^3 - 2</b>. Por último, se intuye que los valores de las funciones derivadas para <b>-2, 0 y 2 son -92, 0 y -28</b> respectivamente.  Conociendo estos datos el equipo de investigadore desea realizar una interpolación para estos datos por 4 diferentes métodos, con la finalidad de comparar los resultados, estos métodos son: Taylor, Lagrange, Hermite, y Polinómica a trozos (Interpolador por splines).

Además, para la interpolación de Taylor, se desea aproximar al punto x = 1, con un máximo de 3 derivadas.
