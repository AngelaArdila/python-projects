# Guardar en una estructura los precios de los articulos articulos
# Ejemplo: codigo,articulo

from optparse import Values
import re
from tkinter import Y
nombre_articulo = ""
ruta_proyecto = "C://Users/ECUADOR/Documents/python_projects/calculo_ventas_archivos/"
precios = {}
structura_datos_clientes = {}
venta_total = {}

with open(ruta_proyecto + "precio_articulos.txt", "r") as archivo_precios:
    next(archivo_precios)
    for linea_sin_salto in archivo_precios:

        linea = linea_sin_salto.replace("\n", "")
        linea_split = linea.split(',')
        precios[linea_split[0]] = {
            "precio": float(linea_split[1]),
            "total": 0
        }


# Guardar en una estructura y un archivo llamado (clientes.txt) los clientes que han comprado articulos
# Ejemplo: cedula,nombre

with open(ruta_proyecto + "ventas_brutas.txt", "r") as datos_ventas_brutas, \
        open(ruta_proyecto + "clientes.txt", "w") as datos_clientes:

    next(datos_ventas_brutas)
    for clientes_ventas_bruta in datos_ventas_brutas:
        split_clientes_ventas = clientes_ventas_bruta.split(",")
        structura_datos_clientes[split_clientes_ventas[0]] = {
            "nombre": split_clientes_ventas[1]
        }

    for k, v in structura_datos_clientes.items():
        datos_clientes.write(k + "," + v["nombre"] + "\n")

# Guardar en una estructura y un archivo llamado (venta_total.txt) las ventas totales de articulos
# Ejemplo: codigo_articulo,nombre_articulo,venta_total

with open(ruta_proyecto + "ventas_brutas.txt", "r") as datos_ventas_brutas:

    next(datos_ventas_brutas)

    for compra_de_articulos_sin_salto in datos_ventas_brutas:
        compra_de_articulos = compra_de_articulos_sin_salto.replace("\n", "")
        spli_compra_articulos = compra_de_articulos.split(",")
        nombre_articulo = spli_compra_articulos[3].replace("kg", "")
        codigo_producto = spli_compra_articulos[2]
        unidades_producto = spli_compra_articulos[4]

        if codigo_producto in precios and "unidades" in precios[codigo_producto]:
            precios[codigo_producto]["unidades"] += float(unidades_producto)
            precios[codigo_producto]["total"] += float(
                unidades_producto) * precios[codigo_producto]["precio"]
        else:
            precios[codigo_producto]["unidades"] = float(unidades_producto)
            precios[codigo_producto]["total"] += float(
                unidades_producto) * precios[codigo_producto]["precio"]
        total_unidad = precios[codigo_producto]["total"]

with open(ruta_proyecto + "venta_total.txt", "w") as informe_ventas:

    for i_codigo, j in precios.items():
        total = j["total"]

        informe_ventas.write("codigo:{}\ttotal:{}\n".format(
            i_codigo, total))


print(precios)
# escribir total en archivo

# print(precios)
