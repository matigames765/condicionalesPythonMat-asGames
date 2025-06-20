#Calculadora simple
#Pedí dos números y una operación (+, -, *, /) y realizá la operación.

number1 = int(input("Ingrese el primer numero: "))

number2 = int(input("Ingrese el segundo numero: "))

operador = str(input("Ingrese + (suma) o - (resta) o * (multiplicacion) o / (division) segun la operacion: "))

if(operador == "+"):
    print(f'{number1} + {number2} = {number1 + number2}')
elif(operador == "-"):
    print(f'{number1} - {number2} = {number1 - number2}')
elif(operador == "*"):
    print(f'{number1} x {number2} = {number1 * number2}')
elif(operador == "/"):
    print(f'{number1} / {number2} = {number1 / number2}')
else:
    print("Operador no valido")