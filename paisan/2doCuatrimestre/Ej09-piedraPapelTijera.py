print("Para jugar al Piedra, Papel o Tijera cada jugador debe seleccionar un elemento para jugar.")
print("Si queres elegir Piedra ingresa 0.")
print("Para Papel, selecciona 1.")
print("Y si queres elegir Tijera, selecciona 2.\n")

jugador1 = int(input("Jugador 1 elija una opcion: "))
jugador2 = int(input("Ahora Jugador 2 elija su opcion: "))

if jugador1 == 0:
    seleccion1 = "Piedra"
elif jugador1 == 1:
    seleccion1 = "Papel"
elif jugador1 == 2:
    seleccion1 = "Tijera"

if jugador2 == 0:
    seleccion2 = "Piedra"
elif jugador2 == 1:
    seleccion2 = "Papel"
elif jugador2 == 2:
    seleccion2 = "Tijera"

if (jugador1 == 2 and jugador2 == 0):
    print(seleccion1,"vs.",seleccion2)
    print("Gano jugador 2.", seleccion2,"le gana a",seleccion1)

elif (jugador1 == 0 and jugador2 == 2):
    print(seleccion1,"vs.",seleccion2)
    print("Gano jugador 1.", seleccion1,"le gana a",seleccion2)

elif (jugador1 > jugador2):
    print(seleccion1,"vs.",seleccion2)
    print("Gano jugador 1.", seleccion1,"le gana a",seleccion2)

elif (jugador2 > jugador1):
    print(seleccion1,"vs.",seleccion2)
    print("Gano jugador 2.", seleccion2,"le gana a",seleccion1)
    
elif (jugador1 == jugador2):
    print(seleccion1,"vs.",seleccion2)
    print("\nEmpate.\n")


# LEER: Carlos, no se por qué los print de los elif me aparecen como listas en vez de como strings.
#       Lo intenté solucionar pero preferí seguir con los demas ejercicios.