# Escritura de tabla dado un numero
import re
from inspect import formatannotation
from tkinter import Y


def tabla_multiplicar(numero):
    with open("tabla_{}.txt".format(numero), "w") as file:
        for i in range(1, 11):
            resultado = numero * i
            file.write("{}x{}={}\n".format(numero, i, resultado))


tabla_multiplicar(2)

# Leer el archivo formatoMultiplicacion.txt con formato de tabla y
#   reemplazar en un archivo llamado resultadoMultiplicacion.txt
#   los signos # con el respectivo resultado de cada multiplicacion


def leer_formatannotation():
    with open("formatoMultiplicacion.txt", "r") as archivo_lectura, open('resultadoMultiplicacion.txt', 'w') as archivo_escritura:
        for x in archivo_lectura:
            lista_valores = re.findall(r'-?\d+\.?\d*', x)
            multiplicador = int(lista_valores[0])
            multiplicado = int(lista_valores[1])
            resultado_operacion = multiplicador * multiplicado

            archivo_escritura.write("{}x{}={}\n".format(
                multiplicador, multiplicado, resultado_operacion))


leer_formatannotation()
