from flask import Flask, jsonify, request
import json

# nombre, cedula, pagoMesActual, huella
# Casos prueba: Ningun campo 400, cedula inexistente 400 y contraseña error 403

app = Flask(__name__)

def leer_json_archivo(nombre_archivo):
    with open(nombre_archivo) as leer_productos:
        return json.load(leer_productos)

@app.post("/registro_gym")
def registro_gym():
    cliente_registrados= request.json
    clientes = leer_json_archivo("clientes_gym.json")
    numero_cedula=cliente_registrados["cedula"]
    ingreso_hoy=clientes[numero_cedula]["intentos"]
    nombre_cliente=clientes[numero_cedula]["nombre"]
   
   
    cliente_presente={}
    
   
    
    if cliente_registrados["cedula"] in clientes and cliente_registrados["cedula"]== numero_cedula :
          estado_cliente = clientes[numero_cedula]["estado"]
          cliente_presente["nombre"]=nombre_cliente
          
          
          
    elif  cliente_registrados["cedula"]=="":
        return "ingrese su numero de cedula"
    else:
        return"no estas registrado"
    if estado_cliente > 0:
        cliente_presente["estado"]= estado_cliente 
        cliente_presente["intentos"] = ingreso_hoy + 1
        
        print(ingreso_hoy)
    else:
        print("inscribete ya")
    print(cliente_presente)
    
    return jsonify ({"cliente":cliente_presente})
if "main" in __name__:
    app.run()
