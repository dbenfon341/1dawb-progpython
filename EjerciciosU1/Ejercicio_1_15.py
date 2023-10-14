# Ejercicio 2.15
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
# Calcula el interés: capital * (1 + interes)


capital = float(input("Introduce tus ahorros: "))
interes = 0.04
primeraño = capital * (1 + interes)
segundoaño = primeraño * (1 + interes)
terceraño = segundoaño * (1 + interes)
primeraño = round(primeraño, 2)
segundoaño = round(segundoaño, 2)
terceraño = round(terceraño, 2)

print("Ahorros después del primer año:", primeraño)
print("Ahorros después del segundo año:", segundoaño)
print("Ahorros después del tercer año:", terceraño)