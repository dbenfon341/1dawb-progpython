# Ejercicio 2.2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.


def total(horas: int, precio: float):
    return horas * precio


horas = int(input("Horas de trabajo: "))
precio = int(input("Coste por hora: "))
print("Importe total:", + str(total())) 