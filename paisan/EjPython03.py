#Ejercicio de cálculo de superficie de un parque y cálculo de la cantidad necesaria de bloques de pasto que lo deberían cubrir.
import math

import os

os.system('cls')
os.system('clear')

#Valores expresados en centímetros

bloqueLargo = 120
bloqueAncho = 80
costoBloque = 450

parqueLargo = int(input("Cuál es el largo del parque (Ingresar valores en cm)?:    "))
parqueAncho = int(input("Cuál es el ancho del parque (Ingresar valores en cm)?:    "))

bloquesNecLargo = float (parqueLargo / bloqueLargo)
bloquesNecAncho = float (parqueAncho / bloqueAncho)

bloquesNecLargoRed = round (bloquesNecLargo)
bloquesNecAnchoRed = round (bloquesNecAncho)

parqueSuperficieBloque = int(bloquesNecLargoRed * bloquesNecAnchoRed)
parqueSuperficieBloqueCosto = int((bloquesNecLargoRed * bloquesNecAnchoRed) * costoBloque)

montoTotal = parqueSuperficieBloqueCosto
formatoMoneda = "${:,.2f}".format(montoTotal)

supBloque = int(bloqueLargo * bloqueAncho) 
supParque = int(parqueLargo * parqueAncho)
supBloquesTotal = int(parqueSuperficieBloque * supBloque)
desperdicio =  int(supBloquesTotal - supParque)
bloquesDemasAprox = int(desperdicio / supBloque)
bloquesDemasAproxRounded = round(bloquesDemasAprox)

print ("Total de bloques a comprar ",str(parqueSuperficieBloque).rjust(1))
print (" ")
print ("** INFORMACIÓN EXTRA **") 
print ("El costo total a invertir para la compra de los bloques de pasto es de",str(formatoMoneda))
print ("Hay un desperdicio aproximado de",str(desperdicio)," centimetros. Esto se traduce en aproximadamente en",str(bloquesDemasAproxRounded),"bloques.")
