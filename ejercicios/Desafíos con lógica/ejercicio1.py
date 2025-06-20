#Reloj digital
#Pedí una hora en formato 24h y decí si es de mañana (0–12), tarde (13–18) o noche (19–23).

hora = int(input("Ingresa la hora de 0 a 23: "))

if(hora >= 0 and hora <= 12):
    print("La hora ingresada es de mañana")
elif(hora >= 13 and hora <= 18):
    print("La hora ingresada es de tarde")
elif(hora >= 19 and hora <= 23):
    print("La hora ingresada es de noche")
else:
    print("La hora ingresada no es valida")