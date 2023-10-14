# Ejercicio 2.23
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
# pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.


correo = input("Introduce tu correo electrónico: ")
parteanterior = correo.split("@")[0]
nuevocorreo = parteanterior + "@ceu.es"

print("Tu correo con el nuevo dominio es:", nuevocorreo)