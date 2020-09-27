cantidadJugadores = 4
listaJugadores = []

for i in range(1,cantidadJugadores):
    nombreJugador = str(input("Ingrese nombre del jugador: "))
    edadJugador = int(input("Ingrese la edad: "))
    camisetaJugador = int(input("Ingrese el numero de camiseta: "))
    print("")
    listaJugadores.append([nombreJugador,edadJugador,camisetaJugador])

# edadesTotales = sum(listaJugadores[1])
# edadesTotales = map(sum, listaJugadores[1])
edadesTotales = [sum(b) for b in listaJugadores]


print(listaJugadores)
print("")
print(edadesTotales)
