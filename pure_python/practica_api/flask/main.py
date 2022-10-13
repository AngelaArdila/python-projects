from urllib import request
from flask import Flask, jsonify, request
from productos import products

app = Flask(__name__)


@app.route("/hola")
def saludar():
    return jsonify({"name": "Maria", "apellido": "guerrero"})


@app.get("/productos")
def getproductos():
    return jsonify({"productos": products})


@app.get("/productos/<string:producto_name>")
def getproducto(producto_name):
    producto_foun = [
        producto for producto in products if producto["name"] == producto_name]
    if len(producto_foun) > 0:
        return jsonify({"product": producto_foun[0]})
    else:
        return jsonify({"mensajes": "producto no disponible"})


@app.post("/agregar")
def addProductos():
    new_product = {"name": request.json["name"],
                   "price": request.json["price"],
                   "quantity": request.json["quantity"], }
    products.append(new_product)
    print(products)
    with open("agregar_producto.txt", "a")as agregar_lista:
        agregar_lista.write(str(products))
    return jsonify({"products": products})


@app.post("/agregarLista")
def addProductosLista():
    list_product = request.json
    for product_nuevos in list_product:
        products.append(product_nuevos)
        print( products)
    return jsonify({"products":products})


app.run(debug=True, port=5000)
