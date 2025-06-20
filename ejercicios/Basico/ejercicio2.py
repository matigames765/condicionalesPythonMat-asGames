#Par o impar
#Pedí un número al usuario y decí si es par o impar.

number = int(input("Ingresa un numero para saber si es par o impar: "))

if(number % 2 == 0):
    print(f'El numero {number} es par')
else:
    print(f'El numero {number} es impar')
