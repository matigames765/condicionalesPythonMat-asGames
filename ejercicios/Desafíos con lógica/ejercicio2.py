#Login con 3 intentos
#Simulá un login pidiendo usuario y contraseña. Permití hasta 3 intentos.

password_predefinida = "123456"

user_predefinido = "usuario1"

counter = 0

while counter <= 2:
    user = str(input("Ingrese el nombre de usuario: "))
    password = str(input("Ingrese la contraseña: "))

    if(user == user_predefinido and password == password_predefinida):
        print("Datos correctos!")
        acertado = 1
        break
    else:
        print("Datos incorrectos")
        acertado = 0
    
    counter += 1

if (acertado == 0):
    print("Lo siento se te acabaron los intentos")

