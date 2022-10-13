import datetime
from time import time
from flask import Flask, jsonify, Response, request
import random
import json

print("reload: " + str(datetime.datetime.now()))

app = Flask(__name__)


@app.post("/cuentas_bancarias")
def agregar_cuentas_bancarias():

    new_clientes = request.json

    cuentas_bancarias = {}
    with open("cuentas_bancarias.json") as leer_cuentas_bancaria:
        cuentas_bancarias = json.load(leer_cuentas_bancaria)

    for id, y in new_clientes.items():
        cuentas_bancarias[id] = y

    with open("cuentas_bancarias.json", "w") as leer_cuentas_bancaria:
        json.dump(cuentas_bancarias, leer_cuentas_bancaria)

    return jsonify({"diccionario_cuentas_bancarias": cuentas_bancarias})


@app.post("/retiro_bancario")
def transacion_retiro():
    body_retiro = request.json

    cuentas_bancarias = {}
    with open("cuentas_bancarias.json") as leer_cuentas_bancaria:
        cuentas_bancarias = json.load(leer_cuentas_bancaria)

    numero_cuenta = body_retiro["numero_cuenta"]
    if numero_cuenta in cuentas_bancarias:
        cuenta = cuentas_bancarias[numero_cuenta]
        if body_retiro["password"] == cuenta["password"]:
            if cuenta["ahorros"] > body_retiro["retiro"]:
                cuenta["ahorros"] -= body_retiro["retiro"]
                ticket = {"numero_cuenta": numero_cuenta,
                          "nombre": cuenta["nombre"], "retiro": body_retiro["retiro"], "saldo": cuenta["ahorros"]}
                ticket_str = "Fecha: {}, Cuenta: {}, retiro: {}, saldo: {}".format(
                    str(datetime.datetime.now()), numero_cuenta, body_retiro["retiro"], cuenta["ahorros"])

                with open("cuentas_bancarias.json", "w") as leer_cuentas_bancaria:
                    json.dump(cuentas_bancarias, leer_cuentas_bancaria)

                with open("ticket{}.json".format(random.randint(1, 100000)), "w") as archivo_ticket:
                    json.dump(ticket, archivo_ticket)

                print({"ticket": ticket, "ticketFormat": ticket_str})

                return Response(json.dumps({"ticket": ticket, "ticketFormat": ticket_str}),
                                status=200, mimetype='application/json')
            else:
                return Response(json.dumps({}), status=400, mimetype='application/json')
        else:
            return Response(json.dumps({}), status=403, mimetype='application/json')
    return Response(json.dumps({}),
                    status=500, mimetype='application/json')


if "main" in __name__:
    app.run()
