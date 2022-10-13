f = open("C://Users/ECUADOR/Documents/python_projects/proyecto-inicio/data.txt", "r")
print(f.read())
x = str(2)
print(type(x))

y = float(3)
print(y)
print(type(y))
animales = [" gato ", " perro ", " loro "]
a, b, c = animales
print(a)
nombre = "Manuel "
apellido = "Gonzales "
print(nombre + apellido)

h = "world "


def HolaMundo():
    print("hello", h)


HolaMundo()

suName = "Cristina "


def saludo():
    suName = "Bryan "
    print("hola", suName)


saludo()
print("Hola " + suName)


def myMascota():
    global g
    g = "gato "
    print("Mi mascota es un", g)


myMascota()
print(g)
import random

print(random.randrange(1, 20))
nameis = "Gonzalo"
print(nameis[0], ", soy el indice 0")
print(nameis, "su longitud es de", len(nameis))

for c in "Cris":
    print(c)
nombreMujeres = ["Alemania", "Japon", "Rubi", "Dany"]
if "Japon" in nombreMujeres:
    print("Japon pertenece a la lista de nombre de mujeres")

    nombreMujeres[3] = "Lucia"

print(nombreMujeres)
for d in nombreMujeres:
    if d == "Rubi":
        print(d)

set_a = [1, 2, 3, 4, 5]
set_b = [3, 4, 5, 6, 7]
resultadSet_a = sum(set_a)
resultadSet_b = sum(set_b)

# union a y b
cambioSet_a = set(set_a)
cambioSet_b = set(set_b)

set_u = (cambioSet_a.union(cambioSet_b))
print(set_u)


# difencia de a - b
z = cambioSet_a.difference(cambioSet_b)
print(z)

# la suma de cada elemento de a mas la suma de cada elemento de b
set_c = set_a + set_b
resultadSet_c = sum(set_c)
print("3- ", resultadSet_c)