# Aplicar descuentos por compras en cantidad

import os
os.system('cls')
os.system('clear')

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.GREEN}Bienvenido a empresa ALFA." + bcolors.ENDC)

cantidadArtCompra = int(input("Ingrese la cantidad de artículos a comprar: "))
precioPorArt= 1
descuento1000= 5
descuento2000= 10

if cantidadArtCompra < 1001:
    precioFinal = cantidadArtCompra * precioPorArt
elif cantidadArtCompra > 1000 and cantidadArtCompra < 2001:
    precioFinalTmp = ((cantidadArtCompra * precioPorArt) * descuento1000 / 100) - cantidadArtCompra
    precioFinal = abs(precioFinalTmp)
else:
    precioFinalTmp = ((cantidadArtCompra * precioPorArt) * descuento2000 / 100) - cantidadArtCompra
    precioFinal = abs(precioFinalTmp)

print(f"{bcolors.BOLD}Total a pagar: $"  + bcolors.ENDC,round (precioFinal))
print("")