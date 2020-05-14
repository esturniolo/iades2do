#!/usr/bin/python3
import os
from time import sleep

os.system('cls')
os.system('clear')

print ("")
print ("")

print ("----------------------------------------------------------------------------------------------------------------------------------------------------")
print ("El Ministerio de Salud a través de este programa analiza la información cada 4 días debido al índice de contagio. El mismo se triplica cada 96 horas")
print ("----------------------------------------------------------------------------------------------------------------------------------------------------")
print ("")

camasDisponibles= int(input("Por favor ingresar el total de camas de su ciudad: "))
totalInfectadosHoy = int(input("Por favor ingrese cuantos infectados hay al día de hoy: "))

dia = 1

print ("")
print ("Camas Disponibles:",camasDisponibles)

camasDisponibles = camasDisponibles - totalInfectadosHoy
nuevosInfectados = totalInfectadosHoy

sleep(5)

while camasDisponibles > totalInfectadosHoy:
    print ("Día",dia,". Nuevos Total infectados:",nuevosInfectados,". Quedan",camasDisponibles,"camas disponibles")
    sleep(3)
    print ("")

    #nuevosInfectados = totalInfectadosHoy*3
    nuevosInfectados = nuevosInfectados*3

    if totalInfectadosHoy < 1:
        nuevosInfectados = totalInfectadosHoy + 1 
        print("*************************")
        print("*        ALERTA         *")
        print("*************************")
        print("")
        sleep(0.5)
        print("*************************")
        print("*        ALERTA         *")
        print("*************************")
        print("")
        sleep(0.5)
        print("Oh! Se te filtró un extranjero coronaviruseado!. Preparate")
        print("")
        sleep(2)

    dia = dia+1
    print ("Dia",dia,"...")
    sleep(2)
    print ("")
    dia = dia+1
    print ("Dia",dia,"...")
    sleep(2)
    print ("")
    dia = dia+1
    if totalInfectadosHoy == 1:
        totalInfectadosHoy = 3
        camasDisponibles = camasDisponibles - totalInfectadosHoy + 1
    #totalInfectadosHoy = totalInfectadosHoy + nuevosInfectados
    camasDisponibles = camasDisponibles - nuevosInfectados
#    if nuevosInfectados > 1:
#        print ("Nuevos infectados del período:",totalInfectadosHoy - nuevosInfectados)
#        print ("")
#    else:
#        print ("Nuevos infectados del período:", nuevosInfectados)
#        print ("")
    sleep(2)

print ("")
print ("")

print ("Total infectados:",nuevosInfectados)
print ("Total de camas disponibles:",camasDisponibles)
print ("El total de infectados es superior al total de camas. TODOS VAMOS A MORIR.")
print ("")
print ("      |")
print ("   -------")
print ("      |")
print ("      |")
print ("      |")
print (" R.I.P. País")
print ("")
print ("")