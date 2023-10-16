# Ejercicio 2.1
# Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.



def saludo():
    nombre = input("Escribe tu nombre: ")
    return nombre


print(f"Hola {saludo()}")