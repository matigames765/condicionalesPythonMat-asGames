#Aprobación con condiciones
#Pedí dos notas. Si ambas son mayores a 6, aprobó. Si una sola es menor a 6, rinde recuperatorio. Si ambas son menores, repite.

nota1 = float(input("Ingrese la primer nota: "))

nota2 = float(input("Ingrese la segunda nota: "))

if(nota1 >= 6 and nota2 >= 6):
    print("El alumno aprobo")
elif(nota1 >= 6 or nota2 >= 6):
    print("El alumno rinde recuperatorio")
else:
    print("El alumno repite")
