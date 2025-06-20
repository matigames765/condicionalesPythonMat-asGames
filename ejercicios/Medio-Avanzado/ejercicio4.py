#Categoría por edad
#Pedí la edad y asigná una categoría: "Niño", "Adolescente", "Adulto", "Adulto mayor".

edad = int(input("Ingrese la edad: "))

if (edad < 12):
    categoria = "Niño"
elif(edad < 18):
    categoria = "Adoslecente"
elif(edad < 60):
    categoria = "Adulto"
else:
    categoria = "Adulto mayor"

print(f"Segun su edad su categoria es {categoria}")