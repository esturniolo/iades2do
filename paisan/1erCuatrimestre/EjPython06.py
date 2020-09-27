#Cajero Automático (Entregar billetes de 0 a N) Ver divisonesy restos. Para ver si se puede hacer mas fácil.

import os
os.system('cls')
os.system('clear')

dineroARetirar = int(input("Ingrese el monto a retirar en múltiplos de $10: "))

dineroAEntregar = 0
dineroAEntregar1000= 0
dineroAEntregar500= 0
dineroAEntregar200= 0
dineroAEntregar100= 0
dineroAEntregar50= 0
dineroAEntregar20= 0
dineroAEntregar10= 0

while dineroARetirar > dineroAEntregar:
    dineroAEntregar = dineroAEntregar + 1000
    if dineroARetirar == dineroAEntregar:
        dineroAEntregar = dineroAEntregar1000
        break
    elif dineroAEntregar > dineroARetirar:
        dineroAEntregar = dineroAEntregar - 1000
        break

while dineroARetirar > dineroAEntregar:
    dineroAEntregar = dineroAEntregar + 500
    if dineroARetirar == dineroAEntregar:
        dineroAEntregar = dineroAEntregar500
        break
    elif dineroAEntregar > dineroARetirar:
        dineroAEntregar = dineroAEntregar - 500
        break

while dineroARetirar > dineroAEntregar:
    dineroAEntregar = dineroAEntregar + 200
    if dineroARetirar == dineroAEntregar:
        dineroAEntregar = dineroAEntregar200
        break
    elif dineroAEntregar > dineroARetirar:
        dineroAEntregar = dineroAEntregar - 200
        break

while dineroARetirar > dineroAEntregar:
    dineroAEntregar = dineroAEntregar + 100
    if dineroARetirar == dineroAEntregar:
        dineroAEntregar = dineroAEntregar100
        break
    elif dineroAEntregar > dineroARetirar:
        dineroAEntregar = dineroAEntregar - 100
        break

while dineroARetirar > dineroAEntregar:
    dineroAEntregar = dineroAEntregar + 50
    if dineroARetirar == dineroAEntregar:
        dineroAEntregar = dineroAEntregar50
        break
    elif dineroAEntregar > dineroARetirar:
        dineroAEntregar = dineroAEntregar - 50
        break

while dineroARetirar > dineroAEntregar:
    dineroAEntregar = dineroAEntregar + 20
    if dineroARetirar == dineroAEntregar:
        dineroAEntregar = dineroAEntregar20
        break
    elif dineroAEntregar > dineroARetirar:
        dineroAEntregar = dineroAEntregar - 20
        break

while dineroARetirar > dineroAEntregar:
    dineroAEntregar = dineroAEntregar + 10
    if dineroARetirar == dineroAEntregar:
        dineroAEntregar = dineroAEntregar10
        break
    elif dineroAEntregar > dineroARetirar:
        dineroAEntregar = dineroAEntregar - 10
        break


print("fin")
print(dineroAEntregar)
print(dineroAEntregar1000)
print(dineroAEntregar500)
print(dineroAEntregar200)
print(dineroAEntregar100)
print(dineroAEntregar50)
print(dineroAEntregar20)
print(dineroAEntregar10)