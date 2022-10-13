
from flask import Flask, jsonify, request
import json
# flask --app main.py --debug run

app = Flask(__name__)


@app.post("/productos")
def productos():
    productos_tienda = {}
    factura_compra = {}
    compras_cliente = request.json
    cantidad_producto = 0
    lista_productos_comprados = []

    with open("productos.json") as leer_productos:
        productos_tienda = json.load(leer_productos)

    for i in compras_cliente:
        codigo_producto = i["codigo"]
        unidades_producto = i["unidades"]

        print(i["codigo"])
        if codigo_producto in productos_tienda:
            nombre_producto = productos_tienda[codigo_producto]["name"]
            precio_unitario = productos_tienda[codigo_producto]["precio_unidad"]
            precio_total = float(unidades_producto*precio_unitario)
            lista_productos_comprados.append({"name":nombre_producto})

            i.update({"name": nombre_producto,
                     "precio_unidad": precio_unitario, "precio_total": precio_total})
            if not "name" in factura_compra:
                factura_compra["productos"] = lista_productos_comprados
                cantidad_producto = len(factura_compra["productos"])
            else:
                print("no")

            if "total" in factura_compra:
                    factura_compra["total"] += precio_total
                    factura_compra["cantidad_producto"] = cantidad_producto
                    

            else:
                        factura_compra["total"] = precio_total
                       
    with open ("factura.json", "w") as guardar_factura:
        json.dump(factura_compra,guardar_factura)
        
        print(factura_compra)

    print(compras_cliente)
    return jsonify(factura_compra)
   
    


print(__name__)
if "main" in __name__:
    app.run()
