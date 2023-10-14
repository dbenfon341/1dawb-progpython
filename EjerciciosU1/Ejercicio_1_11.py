# Ejercicio 2.11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y 
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n+1) / 2


numero = int(input("Introduce un número: "))

if numero < 1:
    print("Por favor, introduce un número entero positivo.")
else:
    numeros = numero * (numero+1) // 2
    print(numeros)