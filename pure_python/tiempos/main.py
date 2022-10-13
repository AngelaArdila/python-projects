import time

# 1. Concatenar los numeros desde un numero 0 hasta un 5 000 000 separados por coma
# 2. Tomar el tiempo que se tomo  el proceso
"""
Guardar en un archivo numeros_concatenados.txt lo siguiente:

Tiempo total en milisegundos: XXX ms
Numeros concatenados desde 0 hasta 5 000 000:
1,2,3,4,5,6,7...100
101,102,........200
............5000000
"""

"""
tiempo_inicio = time.time()

"""
inicio = time.time()

cadenaArchivo = ""

for y in range(1, 50000):

    if y % 100 == 0:
        cadenaArchivo = "{}{},\n".format(cadenaArchivo, y)
        
    else:
        cadenaArchivo = "{}{},".format(cadenaArchivo, y)



fin = time.time()
tiempo_total = fin-inicio
convercion = tiempo_total*1000
with open("conteo_tiempo_numeros.txt", "w") as conteo:
    conteo.write(cadenaArchivo + "\n")
    conteo.write(str("{}-{}={} => {} ms".format(inicio, fin, tiempo_total, convercion)))
