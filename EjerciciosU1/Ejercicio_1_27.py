# Ejercicio 2.27
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena 
# con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce su precio: "))
unidades = int(input("Introduce las unidades: "))
total = precio * unidades

print (f"Nombre del producto: {producto} \nPrecio unitario: {precio:09.2f} \nNúmero de unidades: {unidades:03d} \nCoste total: {total:011.2f}")