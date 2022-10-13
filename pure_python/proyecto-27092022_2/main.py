from re import I
from tkinter import Y


amigos_dict = {
    "dario": {
        "amigos": [
            "ernesto", "peterson"
        ]
    },
    "ernesto": {
        "amigos": [
            "peterson", "dario", "nataly", "karen"
        ]
    },
    "peterson": {
        "amigos": [
            "craig", "ernesto", "jose"
        ]
    }
}
# Crear una funcion que reciba 2 nombres y permita saber si son amigos
# ejm dario es amigo de ernesto y ernesto es amigo de peterson


def son_amigos(persona_1="", persona_2=""):
    for nombre_amigos, amigos_recorrido in amigos_dict.items():
        for cada_amigo in amigos_recorrido["amigos"]:
            if nombre_amigos == persona_1 and cada_amigo == persona_2:
                print(persona_1, "es amigo de", persona_2)

# son_amigos("dario", "ernesto")
# son_amigos("peterson", "ernesto")


def buscar_persona_con_mas_amigos():
    persona_elegida = ""
    persona_elegida_min = ""
    numero_max_amigos = 0
    mumero_minimo = 100
    for quien_tiene_mas_amigos, cuantos_amigos in amigos_dict.items():
        cantidad_amigos = len(cuantos_amigos["amigos"])
        if numero_max_amigos < cantidad_amigos:
            numero_max_amigos = cantidad_amigos
            persona_elegida = quien_tiene_mas_amigos
        if mumero_minimo > cantidad_amigos:
            mumero_minimo = cantidad_amigos
            persona_elegida_min = quien_tiene_mas_amigos

    print(persona_elegida, "tiene",  numero_max_amigos, "amigos")
    print(persona_elegida_min, "tiene", mumero_minimo, "amigos")


buscar_persona_con_mas_amigos()
def pertencen_grupo_amigos(persona_del_grupo , pertenecen_al_grupo):
   amigos_dict.get(persona_del_grupo)

   for item_keyss , item_valuess in amigos_dict.items():
       for recorrido_item_valuees in  item_valuess["amigos"]:
           if persona_del_grupo == item_keyss and pertenecen_al_grupo == recorrido_item_valuees  :
            print(persona_del_grupo," es amigo de ", pertenecen_al_grupo )
          
pertencen_grupo_amigos("dario" , "peterson")    
pertencen_grupo_amigos("dario" ,  "ernesto")
pertencen_grupo_amigos("dario" , "jose")