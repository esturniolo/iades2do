#!/usr/local/bin/python3

#Ejercicio de cálculo de finalización de deuda, dados los importes de gastos y sueldos, incluyendo aguinaldos.

import os

os.system('cls')
os.system('clear')

salario = 10000
medioAguinaldo = 5000
gastosFijos = 8500
deuda = 50000
meses = [1,2,3,4,5,6,7,8,9,10,11,12]
totalMeses = 0

while deuda > 0: 
    for i in meses:
        if i == 3 or i == 6:
            sobranteSalario= salario - gastosFijos
            deuda = deuda - sobranteSalario - medioAguinaldo
            totalMeses= totalMeses + 1
        else:
            sobranteSalario = salario - gastosFijos
            deuda = deuda - sobranteSalario
            totalMeses= totalMeses + 1


print("La deuda finalizó en",totalMeses, "meses.")