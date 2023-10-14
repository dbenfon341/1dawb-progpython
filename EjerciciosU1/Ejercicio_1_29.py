#Ejercicio 1.29
#Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
#Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
#El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
#El pseudocódigo debes incluirlo como comentarios en el programa de Python.


# Inicio
# 
#     Escribe "Introduce tu nombre: "
#     Lee nombre
#     Si nombre == "" entonces
#       nombre = "Desconocido"
# 
#     Escribe "Introduce tu edad: "
#     Lee edad
#     Mientras edad (<= 0 or edad >= 125) hacer
#       Escribe "Introduce una edad válida: "
#       Lee edad
# 
#     Escribe "Te llamas" + nombre + "y tienes" + edad + "años, te quedan aún" + (125 - edad) + "años por cumplir."
# 
# Fin


nombre = input("Introduce tu nombre: ")
if nombre == (""):
    nombre = ("Desconocido")

edad = int(input("Introduce tu edad: "))
while edad <= 0 or edad >= 125:
    edad = int(input("Introduce una edad válida: "))

print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {125 - edad} años por cumplir.")