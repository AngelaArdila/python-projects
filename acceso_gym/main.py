from flask import Flask, jsonify, request, Response
import json

# nombre, cedula, pagoMesActual, huella
# Casos prueba: Ningun campo 400, cedula inexistente 400 y contraseña error 403

app = Flask(__name__)


def leer_json_archivo(nombre_archivo):
    with open(nombre_archivo) as leer_productos:
        return json.load(leer_productos)


@app.post("/registro_gym")
def registro_gym():
    cliente_registrados = request.json
    clientes = leer_json_archivo("clientes_gym.json")
    
   

    cliente_presente = {}

    if "cedula" not in cliente_registrados or cliente_registrados["cedula"] not in clientes:
        return Response(json.dumps({}), status=400, mimetype='application/json')
    elif cliente_registrados["cedula"] in clientes:
        numero_cedula = cliente_registrados["cedula"]
        ingreso_hoy = clientes[numero_cedula]["intentos"]
        nombre_cliente = clientes[numero_cedula]["nombre"]
        estado_cliente = clientes[numero_cedula]["estado"]
        huella_digital=cliente_registrados["huella"]
        
        
        cliente_presente["nombre"] = nombre_cliente
        
        
       
        # validar huella
        if  "huella" not in  cliente_registrados or not huella_digital==clientes[numero_cedula]["huella"]:
             return Response(json.dumps({}), status=400, mimetype='application/json')
             
            
        if estado_cliente > 0:
            cliente_presente["estado"] = estado_cliente
            cliente_presente["intentos"] = ingreso_hoy + 1
        else:
            print("inscribete ya")
        
        return Response(json.dumps(cliente_presente), status=200, mimetype='application/json')

    return Response(json.dumps({}), status=400, mimetype='application/json')


if "main" in __name__:
    app.run()
