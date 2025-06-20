#Triángulo válido
#Pedí tres lados y verificá si pueden formar un triángulo.

lado1 = int(input("Ingresa el lado 1: "))

lado2 = int(input("Ingresa el lado 2: "))

lado3 = int(input("Ingresa el lado 3: "))

if(lado1 >= lado2 and lado1 >= lado3):
    if((lado2 + lado3) > lado1):
        print("Pueden formar un triangulo")
    else:
        print("No pueden formar un triangulo")
elif(lado2 >= lado3):
    if((lado1 + lado3) > lado2):
        print("Pueden formar un triangulo")
    else:
        print("No pueden formar un triangulo")
else:
    if((lado2 + lado3) > lado3):
        print("Pueden formar un triangulo")
    else:
        print("No pueden formar un triangulo")
