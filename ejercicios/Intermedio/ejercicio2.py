#Múltiplo de otro número
#Pedí dos números e indicá si el primero es múltiplo del segundo.

number1 = int(input("Ingrese el primer numero: "))

number2 = int(input("Ingrese el segundo numero: "))

if(number1 % number2 == 0):
    print(f'El numero {number1} es multiplo de {number2}')
else:
    print(f'El numero {number1} no es multiplo de {number2}')