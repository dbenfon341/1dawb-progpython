# Ejercicio 2.2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
# Recibe horas y coste y retorna el importe total.

def total():
    horas = int(input("Horas de trabajo: "))
    precio = int(input("Coste por hora: "))
    maximo = horas * precio
    return print(f"Importe total: {maximo}")


total()