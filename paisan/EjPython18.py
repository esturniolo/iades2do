# Aplicar descuentos por compras en cantidad con otro criterio y comentar cual es el mas barato sobre un total de N compras.

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
mejorPrecioA = []
mejorPrecioB = []
precioPorArt= 1
descuento1000A= 5
descuento2000A= 10
descuento1000B= 12.5
descuento2000B= 25
cancelar = "n"
 
print(f"{bcolors.BLUE}Bienvenido a Mercado Libre." + bcolors.ENDC)
#cantidadCompras = int(input("Ingrese cuantas compras va a realizar: "))

while cancelar != 'x':
        cantidadArtCompra = int(input("Ingrese la cantidad de artículos a comprar: "))
        for j in empresas:
           if j == 'ALFA':
               if cantidadArtCompra < 1001:
                   precioFinal = cantidadArtCompra * precioPorArt
                   mejorPrecioA.append(precioFinal)
               elif cantidadArtCompra > 1000 and cantidadArtCompra < 2001:
                   precioFinalTmp = ((cantidadArtCompra * precioPorArt) * descuento1000A / 100) - cantidadArtCompra
                   precioFinal = abs(precioFinalTmp)
                   mejorPrecioA.append(precioFinal)
               else:
                   precioFinalTmp = ((cantidadArtCompra * precioPorArt) * descuento2000A / 100) - cantidadArtCompra
                   precioFinal = abs(precioFinalTmp)
                   mejorPrecioA.append(precioFinal)
           else:
               if cantidadArtCompra < 1001:
                   precioFinal = cantidadArtCompra * precioPorArt
                   mejorPrecioB.append(precioFinal)
               elif cantidadArtCompra > 1000 and cantidadArtCompra < 2001:
                   descExcedente1000 = cantidadArtCompra - 1000
                   precioFinalTmp = ((descExcedente1000 * precioPorArt) * descuento1000B / 100) - cantidadArtCompra
                   precioFinal = abs(precioFinalTmp)
                   mejorPrecioB.append(precioFinal)
               else:
                   descExcedente2000 = cantidadArtCompra - 1000
                   precioFinalTmp1000 = ((999 * precioPorArt) * descuento1000B / 100)
                   precioFinalTmp2000 = ((descExcedente2000 * precioPorArt) * descuento2000B / 100) - cantidadArtCompra
                   precioFinalTmp1000 = abs(precioFinalTmp1000)
                   precioFinalTmp2000 = abs(precioFinalTmp2000)
                   precioFinal = precioFinalTmp1000 + precioFinalTmp2000
                   mejorPrecioB.append(precioFinal)
        cancelar = str(input("Para continuar presione ENTER o x para terminar: "))


print("")
if sum(mejorPrecioA) == sum(mejorPrecioB):
    print("ALFA y BETA tienen los mismos precios.")
elif sum(mejorPrecioA) > sum(mejorPrecioB):
    print("BETA es mas barato.")
    print("$",round(sum(mejorPrecioB)))
else:
    print("ALFA es mas barato.")
    print("$",round(sum(mejorPrecioA)))
print("")
