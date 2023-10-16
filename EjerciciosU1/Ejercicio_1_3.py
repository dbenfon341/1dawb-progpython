# Ejercicio 2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.


temperatura = int(input("Introduce la temperatura Celsius para que pueda pasarla a Fahrenheit: "))
temperatura = ((temperatura*9/5)+32)
print("La temperatura en Fahrenheit es:", temperatura)