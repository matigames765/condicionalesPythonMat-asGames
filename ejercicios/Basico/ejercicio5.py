#Mayor de dos números
#Pedí dos números e imprimí cuál es mayor o si son iguales.

number1 = int(input("Ingrese el numero 1: "))

number2 = int(input("Ingrese el numero 2: "))

if(number1 > number2):
    print(f'El numero {number1} es mayor a {number2}')
elif(number2 > number1):
    print(f'El numero {number2} es mayor a {number1}')
else:
    print("Los numeros ingresados son iguales")