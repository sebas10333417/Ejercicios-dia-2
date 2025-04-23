#El usuario debe escribir 3 numeros y el sistema debe arrojar cual es el menor.

Num1 = int(input("Por favor ingresa un numero: "))
Num2 = int(input("Por favor ingresa otro numero: "))
Num3 = int(input("Por favor ingresa otro numero: "))
if Num1 < Num2:
    menor = Num1

else:
    menor = Num2

if menor < Num3:
    menor = menor

else:
    menor = Num3

print("El numero menor es: ", menor)