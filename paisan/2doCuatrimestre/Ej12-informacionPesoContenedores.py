cantidadContenedores = 11
listaPuerto1 = []
listaPuerto2 = []
listaPuerto3 = []

for i in range(1,cantidadContenedores):
    print("Contenedor",i)
    orden= int(input("Ingrese el numero de Orden: "))
    pesoContenedor= int(input("Ingrese el peso del Contenedor: "))
    puertoDestino= int(input("Ingrese puerto de destino: "))
    if (puertoDestino == 1):
        listaPuerto1.append(pesoContenedor)
    elif (puertoDestino == 2):
        listaPuerto2.append(pesoContenedor)
    elif (puertoDestino == 3):
        listaPuerto3.append(pesoContenedor)

puerto1 = sum(listaPuerto1)
puerto2 = sum(listaPuerto2)
puerto3 = sum(listaPuerto3)

pesoTotal = sum(listaPuerto1) + sum(listaPuerto2) + sum(listaPuerto3)

pesoTotalPromedio = pesoTotal / 10

print("")
print("El peso total para el Puerto 1 es:",puerto1)
print("El peso total para el Puerto 1 es:",puerto2)
print("El peso total para el Puerto 1 es:",puerto3)
print("")
print("El peso total a transportar del buque es de :",pesoTotal)
print("")
print("El promedio por contenedor es:",pesoTotalPromedio)
