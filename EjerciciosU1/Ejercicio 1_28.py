#Ejercicio 1.28
#Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
#El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
#Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
#El pseudocódigo debes incluirlo como comentarios en el programa de Python.


# Inicio
# 
#     Escribe "Introduce un número: "
#     Lee a
#     Escribe "Introduce otro número: "
#     Lee b
# 
#     Si (a == b) entonces
#         Escribe "Los números no pueden ser iguales."
#     Sino
#         Si (a < b) entonces
#           cantidadnumeros = b - a
#           Escribe "El número es el" + a + "y entre ellos existen" + cantidadnumeros + "números enteros."
#         Sino
#           cantidadnumeros = a - b
#           Escribe "El número es el" + b + "y entre ellos existen" + cantidadnumeros + "números enteros."
# 
# Fin


a = int(input("Introduce un número entero: "))
b = int(input("Introduce otro número entero: "))

if a == b:
    print("Los números no pueden ser iguales.")
elif a < b:
    cantidadnumeros = b - a
    print(f"El número menor es el {a} y entre ellos existen {cantidadnumeros} números enteros.")
else:
    cantidadnumeros = a - b
    print(f"El número menor es el {b} y entre ellos existen {cantidadnumeros} números enteros.")