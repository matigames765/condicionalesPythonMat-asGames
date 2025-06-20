#Año bisiesto
#Pedí un año e indicá si es bisiesto o no.

anio = int(input("Ingrese un año para saber si es bisiesto o no: "))


if(anio % 4 != 0):
    print(f'El año {anio} no es bisiesto')
elif(anio % 100 == 0 and anio % 400 != 0):
    print(f'El año {anio} no es bisiesto')
else:
    print("El año es bisiesto")