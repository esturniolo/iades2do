#!/usr/bin/python3

#Ejercicio de cálculo de precio de un producto, el dinero disponible y el sobrante.

import os

os.system('cls')
os.system('clear')

print ("")

precioEmpanadas = int(input("Cuanto cuesta cada empanada?:     "))

def preguntarDinero():
    global dineroEfectivo 
    correcto=False
    num=0
    while(not correcto):
        try:
            dineroEfectivo = int(input("Cuanto dinero tengo? (No pongas los centavos que no los quiere nadie. Solo número redondos):    "))
            correcto=True
        except ValueError:
            print('No te pases de gracioso y poné lo que tenés en la billetera')
     
    return num
 
numero = preguntarDinero()

totalEmpanadas = dineroEfectivo // precioEmpanadas
dineroSobrante = dineroEfectivo % precioEmpanadas

if dineroEfectivo < 0: 
    print ("Estás debiendo guita y encima querés comer?")
    print ("")
elif dineroEfectivo == 0:
    print ("Sali a punguear a alguien sino hoy no comés")
    print ("")
elif precioEmpanadas > dineroEfectivo:
    print ("No te alcanza para nada. POBRE!")
    print ("")
else:
    print ("Puedo comprarme",str(totalEmpanadas),"empanadas y me sobraron",str(dineroSobrante),"pesos.")
    print ("")
