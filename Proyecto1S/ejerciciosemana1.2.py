#Se crea una lista de 5 numeros en el cual el usuario debe digitar un numero y el sistema le indicara si esta dentro de la lista.

num_validar = int(input("ingresa un numero del 1 al 10 que deseas validar: "))
Lista = [2, 4, 6, 8, 10]
if num_validar in Lista:
    print("El numero esta en la lista." .format(num_validar))
else:
    print("El numero no esta en la lista." .format(num_validar))
