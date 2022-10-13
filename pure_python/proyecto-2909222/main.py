# Registros de filas para saber cuanto valen
# Registro de compra de boleto por cliente
# Registro de clientes con sus respectiva filas compradas
from ast import Not
from distutils.log import error
import re
from turtle import clear


registro_de_asiento = {"fa": {"valor": 10, "contador": 0},
                       "fb": {"valor": 20},
                       "fc": {"valor": 30},
                       "fd": {"valor": 40},
                       "ff": {"valor": 50}
                       }


registro_de_compras = [
    {"id": 1, "cedula": "07052", "asiento": "fa", "valor": 10}
]

clientes = {}
total_de_venta = 0
contador_de_hacientos = 0


while True:
    numero_cedula = None
    try:
        print("Ingrece su numero de cedula")
        numero_cedula = input()
        error_numero_cedula = re.findall("[^0-9]", numero_cedula)

        if numero_cedula == "s":
            break
        if numero_cedula == None or numero_cedula == "" or len(error_numero_cedula) > 0:
            print("Digite cedula valida")
            continue

        print("Que asiento desea")
        asignar_asiento = input()
        if not asignar_asiento in registro_de_asiento:
            print("no existe,elija nuevamente")
            continue
        if asignar_asiento in registro_de_asiento:
            dolares_de_valor = registro_de_asiento[asignar_asiento]["valor"]
            total_de_venta = total_de_venta + dolares_de_valor
        print("valor del voleto es:", dolares_de_valor, "$")
       

        len_id = len(registro_de_compras)+1

        registro_de_compras.append(
            {"id": len_id, "cedula": numero_cedula, "asiento": asignar_asiento, "valor": dolares_de_valor})
        print(registro_de_compras)
        
             
            
       
    except:
        print(" tienes un error ")

    clientes.update({numero_cedula: {"asientos": [asignar_asiento]}})

    print(clientes)
    print("total en ventas es :" , total_de_venta ,"$")
    
    if "contador" in registro_de_asiento[asignar_asiento]:
        registro_de_asiento[asignar_asiento]["contador"] +=1
    else:
        registro_de_asiento[asignar_asiento]["contador"]=1
     
     
    print (registro_de_asiento)

    
