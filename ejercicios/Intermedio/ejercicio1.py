#Clasificación de nota
#Pedí una nota del 1 al 10 y mostrá si es "Insuficiente", "Suficiente", "Bien", "Muy bien" o "Excelente".

nota = float(input("Ingrese su nota: "))

if(nota == 10):
    print("Excelente")
elif(nota < 10 and nota >= 9):
    print("Muy bien")
elif(nota < 9 and nota >= 8):
    print("Bien")
elif(nota < 8 and nota >= 7):
    print("Suficiente")
else:
    print("Insuficiente")