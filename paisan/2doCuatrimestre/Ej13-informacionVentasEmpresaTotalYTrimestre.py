import random
meses = 13
ventasPorMes = []

for i in range(1,meses):
    ventas = random.randint(25000,85000)
    ventasPorMes.append(ventas)

ventasTotales = sum(ventasPorMes)

trim1 = ventasPorMes[0] + ventasPorMes[1] + ventasPorMes[2]
trim2 = ventasPorMes[3] + ventasPorMes[4] + ventasPorMes[5]
trim3 = ventasPorMes[6] + ventasPorMes[7] + ventasPorMes[8]
trim4 = ventasPorMes[9] + ventasPorMes[10] + ventasPorMes[11]

porcentajeTrim1 = (trim1 * 100) / ventasTotales
porcentajeTrim2 = (trim2 * 100) / ventasTotales
porcentajeTrim3 = (trim3 * 100) / ventasTotales
porcentajeTrim4 = (trim4 * 100) / ventasTotales


print("")
print("Ventas Totales del año: $",ventasTotales)
print("")
print("El primer trimestre representa un",round(porcentajeTrim1,2),"% del total.")
print("El segundo trimestre representa un",round(porcentajeTrim2,2),"% del total.")
print("El tercer trimestre representa un",round(porcentajeTrim3,2),"% del total.")
print("El cuarto trimestre representa un",round(porcentajeTrim4,2),"% del total.")


# Descomentar lo siguiente para comprobación
# print("")
# print (ventasPorMes)
# print("")
# print(trim1)
# print("")
# print(trim2)
# print("")
# print(trim3)
# print("")
# print(trim4)

# Suma de porcentajes (debe ser 100) 
#print(porcentajeTrim1+porcentajeTrim2+porcentajeTrim3+porcentajeTrim4)










# randomlist = []
# for i in range(0,5):
# n = random.randint(1,30)
# randomlist.append(n)
# print(randomlist)