#Número más grande de tres
#Pedí tres números e indicá cuál es el mayor.

number1 = int(input("Ingresa el numero 1: "))

number2 = int(input("Ingresa el numero 2: "))

number3 = int(input("Ingresa el numero 3: "))

if(number1 > number2 and number1 > number3):
    print(f'{number1} es el mayor')
elif(number2 > number3):
    print(f'{number2} es el mayor')
else:
    print(f'{number3} es el mayor')