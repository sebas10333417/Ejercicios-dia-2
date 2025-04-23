#Se crea una lista con datos almacenados en el cual se le pide al usuario ingresar su nombre y el sistema debera indicarle si su nombre se encuentra en la lista.
Invitados = ["sebastian", "daniel", "camilo"]
Usuario = input("Ingresa tu nombre: ")
if Usuario in Invitados:
    print("Tu nombre se encuentra en la lista de invitado: ")
else:
    print("Tu nombre no esta en la lista de invitados: ")