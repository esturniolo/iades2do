# Aplicar descuentos por compras en cantidad con otro criterio.

import math
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

print(f"{bcolors.BLUE}Bienvenido a empresa BETA." + bcolors.ENDC)

cantidadArtCompra = int(input("Ingrese la cantidad de artículos a comprar: "))
precioPorArt= 1
descuento1000= 12.5
descuento2000= 25

if cantidadArtCompra < 1001:
    precioFinal = cantidadArtCompra * precioPorArt
elif cantidadArtCompra > 1000 and cantidadArtCompra < 2001:
    descExcedente1000 = cantidadArtCompra - 1000
    precioFinalTmp = ((descExcedente1000 * precioPorArt) * descuento1000 / 100) - cantidadArtCompra
    precioFinal = abs(precioFinalTmp)
else:
    descExcedente2000 = cantidadArtCompra - 1000
    precioFinalTmp1000 = ((999 * precioPorArt) * descuento1000 / 100)
    precioFinalTmp2000 = ((descExcedente2000 * precioPorArt) * descuento2000 / 100) - cantidadArtCompra
    precioFinalTmp1000 = abs(precioFinalTmp1000)
    precioFinalTmp2000 = abs(precioFinalTmp2000)
    precioFinal = precioFinalTmp1000 + precioFinalTmp2000

print(f"{bcolors.BOLD}Total a pagar: $"  + bcolors.ENDC,round (precioFinal))
print("")