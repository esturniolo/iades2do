# Aplicar descuentos por compras en cantidad con otro criterio y comentar cual es el mas barato.

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

empresas = ['ALFA','BETA']
mejorPrecio = []
precioPorArt= 1
descuento1000A= 5
descuento2000A= 10
descuento1000B= 12.5
descuento2000B= 25

print(f"{bcolors.BLUE}Bienvenido a Mercado Libre." + bcolors.ENDC)
cantidadArtCompra = int(input("Ingrese la cantidad de artículos a comprar: "))

for i in empresas:
    if i == 'ALFA':
        if cantidadArtCompra < 1001:
            precioFinal = cantidadArtCompra * precioPorArt
            mejorPrecio.append([precioFinal,i])
        elif cantidadArtCompra > 1000 and cantidadArtCompra < 2001:
            precioFinalTmp = ((cantidadArtCompra * precioPorArt) * descuento1000A / 100) - cantidadArtCompra
            precioFinal = abs(precioFinalTmp)
            mejorPrecio.append([precioFinal,i])
        else:
            precioFinalTmp = ((cantidadArtCompra * precioPorArt) * descuento2000A / 100) - cantidadArtCompra
            precioFinal = abs(precioFinalTmp)
            mejorPrecio.append([precioFinal,i])
    else:
        if cantidadArtCompra < 1001:
            precioFinal = cantidadArtCompra * precioPorArt
            mejorPrecio.append([precioFinal,"BETA"])
        elif cantidadArtCompra > 1000 and cantidadArtCompra < 2001:
            descExcedente1000 = cantidadArtCompra - 1000
            precioFinalTmp = ((descExcedente1000 * precioPorArt) * descuento1000B / 100) - cantidadArtCompra
            precioFinal = abs(precioFinalTmp)
            mejorPrecio.append([precioFinal,"BETA"])
        else:
            descExcedente2000 = cantidadArtCompra - 1000
            precioFinalTmp1000 = ((999 * precioPorArt) * descuento1000B / 100)
            precioFinalTmp2000 = ((descExcedente2000 * precioPorArt) * descuento2000B / 100) - cantidadArtCompra
            precioFinalTmp1000 = abs(precioFinalTmp1000)
            precioFinalTmp2000 = abs(precioFinalTmp2000)
            precioFinal = precioFinalTmp1000 + precioFinalTmp2000
            mejorPrecio.append([precioFinal,"BETA"])

print("")
if mejorPrecio[0][0] == mejorPrecio[1][0]:
    print("ALFA y BETA tienen los mismos precios.")
else:
    print("La empresa mas barata es:",min(mejorPrecio)[1])
print("")