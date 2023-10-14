# Ejercicio 2.26
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.


lista = input("Dime los productos que hay en la cesta de la compra (separados con comas): ").split(",")

for i in lista:
    print (i)