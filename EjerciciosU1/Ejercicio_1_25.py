# Ejercicio 2.25
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.


fecha = input("Introduce tu fecha de nacimiento con el formato dd/mm/aaaa: ") #Crea la variable fecha con el valor introducido, debe ser xx/xx/xxxx.
fechadividida = fecha.split("/")                                              #Divide la variable en tres listas cada vez que lee /.
dia = fechadividida[0]
mes = fechadividida[1]
año = fechadividida[2]
print(f"Su fecha de nacimiento es: {dia} / {mes} / {año}")