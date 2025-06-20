#Contraseña correcta
#Pedí una contraseña y comparala con una predefinida. Si coinciden, mostrale acceso concedido.

password_predefinida = "123456"

passsword = str(input("Ingrese su contraseña: "))

if(passsword == password_predefinida):
    print("Contraseña correcta!")
else:
    print("Contraseña incorrecta!")