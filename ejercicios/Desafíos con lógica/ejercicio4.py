#Juego de adivinanza
#Generá un número aleatorio entre 1 y 10. El usuario debe adivinarlo. Indicá si ganó o no.
import random

random_number = random.randint(1,10)

number = int(input("Ingresa un numero entre 1 y 10 para adivinar: "))

if(random_number == number):
    print("Adivinaste el numero")
else:
    print("No adivinaste el numero")
