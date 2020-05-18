#Ejercicio de cálculo del volúmen de cajas y presupuestos de empresas de camiones según las dimensiones de sus camiones. Tomar el mas barato.

from decimal import Decimal
import os

os.system('cls')
os.system('clear')

cajaAlto = float (0.60)
cajaAncho = float (0.60)
cajaProfundidad = float (0.60)

empresasYCostos = []
empresas = ["Andreani","OCA","Transportes del Norte","LogisticAR S.A.", "Serfiglio Hnos."]

cajasATransportar = 10000



for i in empresas:
    print("Empresa:",i)
    costoPorCamion = float(input("Según presupuesto, por favor ingrese el costo por camión: "))
    camionAlto = float(input("Ingrese el alto de los camiones: "))
    camionAncho = float(input("Ingrese el ancho del camion: "))
    camionProfundidad = float(input("Ingrese la profundidad del camión: "))
    
    totalCajasAlto = int(camionAlto/cajaAlto)
    totalCajasAncho = int(camionAncho/cajaAncho)
    totalCajasProfundidad = int(camionProfundidad/cajaProfundidad)

    cajasPorCamion= totalCajasAlto*totalCajasAncho*totalCajasProfundidad
    print("Total cajas: ",cajasPorCamion)

    totalCamiones = cajasATransportar/cajasPorCamion
    print("Total de camiones necesarios: ",int(totalCamiones))

    costoTotal = round(totalCamiones*costoPorCamion,2)
    print("El costo total de",i,"sería de:",int(costoTotal))

    empresasYCostos.append([costoTotal,i])
    
    print("")
    print("-------")
    print("")

print("La empresa mas barata es:",min(empresasYCostos)[1])