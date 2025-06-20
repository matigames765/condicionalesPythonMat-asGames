#Clasificación de año escolar
#Pedí la edad y decí si corresponde a jardín (3–5), primaria (6–12), secundaria (13–17) o universidad (18+).

edad = int(input("Ingrese su edad: "))

if(edad >= 3 and edad <= 5):
    print("La edad corresponde a jardin")
elif(edad >= 6 and edad <= 12):
    print("La edad corresponde a primaria")
elif(edad >= 13 and edad <= 17):
    print("La edad corresponde a secundaria")
elif(edad >= 18):
    print("La edad corresponde a universidad")
else:
    print("La edad no entra en ninguna categoria")