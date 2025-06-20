#Número positivo o negativo
#Pedí un número al usuario e imprimí si es positivo, negativo o cero.

number = int(input("Ingresa un numero para saber si es positivo, negativo o cero: "))

if(number > 0):
    print(f'El numero {number} es positivo')
elif(number < 0):
    print(f'El numero {number} es negativo')
else:
    print('El numero ingresado fue un 0')