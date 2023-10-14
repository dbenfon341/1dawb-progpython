# Ejercicio 2.24
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.


dinero = float(input("¿Cuanto cuesta el producto?: "))
print(dinero[:dinero.find('.')], "euros y", dinero[dinero.find('.')+1:], "céntimos.")