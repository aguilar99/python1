nombre = input("¿Cual es su nombre? \n")
longitudNombre = len(nombre)
print("¡Hola " + nombre.upper() + "! - Su nombre tiene " + str(longitudNombre) + " letras")

for i in range(longitudNombre):
    print(nombre)
