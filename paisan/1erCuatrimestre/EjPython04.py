#Ejercicio de cálculo del volúmen de cajas y ver cuantas entran en un camión.

from decimal import Decimal
import os

os.system('cls')
os.system('clear')

cajaAlto = float (0.60)
cajaAncho = float (0.60)
cajaProfundidad = float (0.60)

camionAlto = float(input("Ingrese el alto del camión: "))
camionAncho = float(input("Ingrese el ancho del camion: "))
camionProfundidad = float(input("Ingrese la profundidad del camión: "))

print("Puede estibar",int(camionAlto/cajaAlto),"cajas.")
print("De ancho entran",int(camionAncho/cajaAncho),"cajas.")
print("Y de profundidad entran",int(camionProfundidad/cajaProfundidad),"cajas")