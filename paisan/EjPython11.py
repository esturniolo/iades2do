#!/usr/local/bin/python3

salario = 10000
medioAguinaldo = 5000
gastosFijos = 8500
deuda = 50000
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
totalMeses = 0

while deuda > 0: 
    for i in meses:
        if meses == "Diciembre":
            sobranteSalario= salario - gastosFijos
            deuda = deuda - sobranteSalario - medioAguinaldo
        else:
            sobranteSalario = salario - gastosFijos
            deuda = deuda - sobranteSalario
    totalMeses= totalMeses + 1


print("La deuda finalizó en",totalMeses, "meses.")