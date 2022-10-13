grupos = [
    ["maria", "belen", "andrea"],
    ["maria", "daniela", "andrea"],
    ["maria", "belen", "gabriela"]
]

integrantes = {
    "maria": {"numero_grupos": 0},
    "belen": {"numero_grupos": 0}
}

for elemento_grupo in grupos:
    for participante in elemento_grupo:
        if participante in integrantes:
            item = integrantes.get(participante)
            item["numero_grupos"] = item["numero_grupos"] + 1
            print(integrantes, "\n\n")
        else:
            integrantes[participante] = {"numero_grupos": 1}
            print(integrantes, "\n\n")
print(integrantes)
