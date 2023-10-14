# Ejercicio 2.17
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario tantas veces como el número introducido.


nom = str(input("Escribe tu nombre de usuario: "))
num = int(input("Escribe otro número: "))

i = 0
while i < num:
    print (nom)
    i += 1