# Ejercicio 2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
# 1.5 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.





def impIva(importe, iva):
    if (iva < 0 or iva > 100):
        iva = 21
        print ("El procentaje debe ser un valor entre 0 y 100... se aplicará el 21%")
        return -1
    
    return importe + (importe * (iva / 100))



importe = float(input("Introduce el importe: "))
iva = float(input())