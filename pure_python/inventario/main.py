# guardar en una estructura y guardar inventario final llamado inventio_final.csv
# Ejemplo A1,pilsener,###
inventario_diccionario_entrada = {}
inventario_diccionario_salida = {}
inventario_final = {}
ruta_proyecto = "C://Users/ECUADOR/Documents/python_projects/inventario/"

with open(ruta_proyecto + "entrada_inventario.csv") as inventario_entrada:
    for i in inventario_entrada:
        sin_salto_productos_inventario = i.replace("\n", "")
        productos_inventario = sin_salto_productos_inventario.split(",")
        codigo_producto = productos_inventario[0]
        nombre_producto = productos_inventario[1]
        unidades_producto = float(productos_inventario[2])

        if codigo_producto in inventario_diccionario_entrada:
            inventario_diccionario_entrada[codigo_producto]["unidades"] += unidades_producto
        else:
            inventario_diccionario_entrada[codigo_producto] = {
                "unidades": unidades_producto, "nombre_producto": nombre_producto
            }

with open(ruta_proyecto + "salida_inventario.csv") as inventario_salida:
    for y in inventario_salida:
        y_sin_salto = y.replace("\n", "")
        lista_inventario_salida = y_sin_salto.split(",")
        salida_codigo_producto = lista_inventario_salida[0]
        salida_nombre_producto = lista_inventario_salida[1]
        salida_cantidad_producto = float(lista_inventario_salida[2])

        if salida_codigo_producto in inventario_diccionario_entrada:
            inventario_diccionario_entrada[salida_codigo_producto]["unidades"] -= salida_cantidad_producto
        else:
            inventario_diccionario_entrada[salida_codigo_producto] = {
                "nombre_producto": salida_nombre_producto, "unidades": -salida_cantidad_producto}
            
      
print(inventario_diccionario_entrada)


with open(ruta_proyecto + "final_inventario.csv", "w") as crear_inventario_final:
    for x , y in inventario_diccionario_entrada.items():
    
     producto = y["nombre_producto"]
     unidades = y["unidades"]
     crear_inventario_final.write("codigo:{}\t,producto:{}\t,unidades:{}\n".format(x,producto,unidades))  

    print("hola")

