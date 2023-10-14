# Ejercicio 2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.


ivageneral = 1.21
ivareducido = 1.10
ivasuperreducido = 1.04

precioarticulo = int(input("Indique el importe del artículo: "))
a = int(input("¿Cuánto IVA desea aplicarle? Por favor, seleccione la opción introduciendo el número correcto:\n 1. General 21% \n 2. Reducido 10% \n 3. Super reducido 4%\n" ))

if a == 1:
    a = precioarticulo * ivageneral 
    print ("El precio final es:",a)
elif a == 2:
    a = precioarticulo * ivareducido
    print ("El precio final es: ",a)
elif a == 3:
    a = precioarticulo * ivasuperreducido
    print ("El precio final es: ",a)
else:
    print ("Introduce un número opción correcta.")