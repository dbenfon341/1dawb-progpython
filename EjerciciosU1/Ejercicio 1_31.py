#
# Ejercicio 1.31 - Lee un n�mero hasta que el n�mero est� en el rango 1-10
#
#
#> Introduce un n�mero: 15
#> Int�ntalo otra vez! (1-10): 0
#> Int�ntalo otra vez! (1-10): 5
#> Correcto!
#
#Inicio
#
#	Escribe "Introduce un n�mero: "
#	Lee num
#	
#	Mientras (num < 1 or num > 10)
#		Escribe "Inténtalo otra vez! (1-10): "
#		Lee num
#	Escribe "Correcto!"
#	
#Fin

num = int(input("Introduce un número: "))

while num < 1 or num > 10:
    num = int(input("Inténtalo otra vez! (1-10): "))
print ("Correcto!")