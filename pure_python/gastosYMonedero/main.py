monedero = {
    1: {
        "descripcion": "1 dolar"
    },
    5: {
        "descripcion": "5 dolares"
    },
    10: {
        "descripcion": "10 dolares"
    },
    50: {
        "descripcion": "50 dolares"
    },
    100: {
        "descripcion": "100 dolares"
    },
}

gastos = [
    {
        "valor": 50
    },
    {
        "valor": 100
    },
    {
        "valor": 1
    },
    {
        "valor": 0.5
    }
]

# Ingresar gastos. Si no existe valor en monedero preguntar por su descripcion y actualizar monedero (se recomienda usar input)
# Imprimir cuanto se ha gastado en total
while True: 
    try:
        print("Ingrese valor de gasto: ")
        ingresar_gasto = input()
        if ingresar_gasto == "s":
            break
        ingresar_gasto_numerico = float(ingresar_gasto)
        if not ingresar_gasto_numerico in monedero:
            print("Ingrese denominacion: ")
            descripcion = input()
            monedero[ingresar_gasto] = {"descripcion": descripcion}
    except:
        print("Error de entrada")

    suma_gastos = 0
    gastos.append({"valor": ingresar_gasto_numerico})

    for elem_cada_gasto in gastos:
        suma_gastos = suma_gastos + elem_cada_gasto["valor"]

    print("Gasto total", suma_gastos)

# Comentar cuando el programa no caiga en bucle infinito
print("monedero", monedero)
print("gastos", gastos)