# Ejercicio 2.8
# Escribir el programa del ejercicio 7 usando solamente dos variables diferentes.


numero = 0
resultado = 0
for a in range(0,2):
    numero = int(input("Introduce un número: "))
    resultado = resultado + numero
    
print("La suma total de los tres números es:", resultado)