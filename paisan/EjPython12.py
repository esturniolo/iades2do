# Ejercicio de progresión de precios y costos según cantidad empleados en fábrica de alfajores.

import os

os.system('cls')
os.system('clear')

cantidadEmpleados = 1
salarioEmpleado = 1000
valorAlfajorUn = float(1.5)
produccionAlfajores = 3000
antiguedadEmpresa = 1

#while totalGanacia > totalSalarios
for cantidadEmpleados in range(1,20,1):
    totalVenta = produccionAlfajores * valorAlfajorUn
    totalSalarios = salarioEmpleado * cantidadEmpleados
    totalGanacia = totalVenta - totalSalarios
    if totalSalarios > totalGanacia:
        print("El total de empleados que puede tener sin reportar pérdidas es de",(cantidadEmpleados-1))
    else:
        print("Seguimos teniendo ganancia durante el mes",(antiguedadEmpresa))
        print("Este mes se generó un total de $",(totalGanacia),"en ganancias.")
    cantidadEmpleados = cantidadEmpleados + 1
    produccionAlfajores = produccionAlfajores + 3000
    valorAlfajorUnTmp = (valorAlfajorUn * 0.1) - valorAlfajorUn
    valorAlfajorUn = abs(valorAlfajorUnTmp)

    antiguedadEmpresa = antiguedadEmpresa + 1

