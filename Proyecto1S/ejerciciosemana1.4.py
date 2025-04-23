#El usuario debera ingresar su edad si la edad es menor que 0 o mayo que 120 el sistema debera indicarle que su edad es incorrecta.
#Si esta dentro del rango permitido el sistema le informara que su edad es permitida.

Edad = int(input("Ingresa tu edad: "))
if Edad < 0 or Edad > 120:
    print("Tu edad no es valida")
else:
    print("Tu edad es valida")

