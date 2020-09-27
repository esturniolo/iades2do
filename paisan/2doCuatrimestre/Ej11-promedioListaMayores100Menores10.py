def Promedio(lista): 
    return sum(lista) / len(lista) 

cantidadNumeros = 20

listaMenor = []
listaMayor = []

for i in range(cantidadNumeros):
    print("Elemento",i)
    numero= int(input("Ingrese el numero del elemento: "))
    if (numero < 10):
        listaMenor.append(numero)
    elif (numero > 100):
        listaMayor.append(numero)

promedioMenor = Promedio(listaMenor) 
promedioMayor = Promedio(listaMayor) 

print("Promedio de los numeros menores a 10:", round(promedioMenor, 2)) 
print("Promedio de los numeros mayores a 100:", round(promedioMayor, 2)) 