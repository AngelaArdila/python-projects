capitulos = {
    "001": [
        "1", "hola", "soy andres"
    ],
    "002": [
        "2", "hola", "soy pedro"
    ],
    "003": [
        "3", "chao", "soy steven"
    ]
}


# contador de palabras

def contar_palabras(palabra=""):
    palabras_repetidas = 0
    for recorrido_capitulos in capitulos.values():
        print(recorrido_capitulos)
        for recorrido_palabras in recorrido_capitulos:
            if recorrido_palabras == palabra:
                palabras_repetidas = palabras_repetidas + 1
    print(palabra, palabras_repetidas, " soy la palabra repetida")


contar_palabras("hola")
