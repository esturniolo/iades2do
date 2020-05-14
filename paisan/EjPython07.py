#!/usr/bin/python3

print ("")


def preguntarEmpanada():
    global precioEmpanadas 
    correcto=False
    num=0
    while(not correcto):
        try:
            precioEmpanadas = int(input("Cuanto cuesta cada empanada?:     "))
            correcto=True
        except ValueError:
            print('Ha-Ha... Muy chistoso. Ahora decime cuanto vale cada empanada.')

    return num

def preguntarDinero():
    global dineroEfectivo 
    correcto=False
    num=0
    while(not correcto):
        try:
            dineroEfectivo = int(input("Cuanto dinero tengo? (No pongas los centavos que no los quiere nadie. Solo número redondos):    "))
            correcto=True
        except ValueError:
            print('No te pases de gracioso y poné lo que tenés en la billetera.')
     
    return num

preguntarEmpanada()
#numero = preguntarDinero()

if precioEmpanadas < 0: 
    print ("Encima te tengo que pagar para comer?")
    print ("")
elif precioEmpanadas == 0:
    print ("Empanadas gratis!!!! Wiiiiiiiiiiii!!!!")
    print ("")
#elif precioEmpanadas > dineroEfectivo:
#    print ("No te alcanza para nada. POBRE!")
#    print ("")
else:
    global totalEmpanadas
    global dineroSobrante
    totalEmpanadas = dineroEfectivo // precioEmpanadas
    dineroSobrante = dineroEfectivo % precioEmpanadas
    preguntarDinero()
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
