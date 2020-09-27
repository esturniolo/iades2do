edad = int(input("Ingrese la edad del jugador: "))

if (edad <= 12):
    print("El jugador es categoria Menor")
elif (edad > 13 and edad <= 18):
    print("El jugador es categoria Cadete")
elif (edad > 18 and edad <= 26):
    print("El jugador es categoria Juvenil")
elif (edad > 26):
    print("El jugador es categoria Mayor")
