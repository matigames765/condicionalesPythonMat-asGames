#Número en rango
#Pedí un número y decí si está entre 10 y 20 (inclusive) o no.

number = int(input("Ingresa un numero: "))

if(number >= 10 and number <= 20):
    print(f'El numero {number} esta entre 10 y 20')
else:
    print(f'El numero {number} no esta entre 10 y 20')