# Ejercicio de progresión de precios y costos según cantidad empleados en fábrica de alfajores.

import os

os.system('cls')
os.system('clear')

cantidadEmpleados = 1
salarioEmpleado = 1000
valorAlfajorUn = float(1.5)
produccionAlfajores = 3000
antiguedadEmpresa = 1
totalGanacia = 1
totalSalarios = 0
listaGanancia =[]

while totalGanacia > totalSalarios:
    totalVenta = produccionAlfajores * valorAlfajorUn
    totalSalarios = salarioEmpleado * cantidadEmpleados
    totalGanacia = totalVenta - totalSalarios
    produccionAlfajores = produccionAlfajores + 3000
    valorAlfajorUnTmp = (valorAlfajorUn * 0.1) - valorAlfajorUn
    valorAlfajorUn = abs(valorAlfajorUnTmp)
    antiguedadEmpresa = antiguedadEmpresa + 1
    listaGanancia.append([totalGanacia,cantidadEmpleados])
    cantidadEmpleados = cantidadEmpleados + 1



print("Se pueden tener",(cantidadEmpleados - 1),"empleados sin reportar pérdidas")
print("La ganancia máxima es de",max(listaGanancia)[0],"con",max(listaGanancia)[1],"empleados")
print("")