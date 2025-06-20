#Calculadora de descuentos
#Pedí el precio y si tiene descuento del 10% (si supera los $10.000) o no.

precio = float(input("Ingrese el precio: "))

if(precio > 10000):
    print(f'Se aplica el descuento del 10% y queda en ${precio * 0.9}')
else:
    print("No se aplica el descuento")