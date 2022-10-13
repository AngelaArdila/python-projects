from flask import Flask, jsonify, request
import json

# nombre, cedula, pagoMesActual, huella
# Casos prueba: Ningun campo 400, cedula inexistente 400 y contraseña error 403

app = Flask(__name__)

@app.pust("/registro_gym")
def hello_world():
    return "<p>Hello, World!</p>"

if "main" in __name__:
    app.run()
