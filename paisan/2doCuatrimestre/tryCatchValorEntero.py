def validarEntero(texto):
    while True:
        try:
            x = int(input(texto))
            break
        except ValueError:
            print ("Error de ingreso de datos")
    return x

def validarEnteroRango(texto,desde,hasta):
    while True:
        try:
            x = int(input(texto))
            if x>= desde and x<=hasta:
                break
        except ValueError:
            print ("Error de ingreso de datos")
    return x

a = validarEntero("ingrese un numero: ")
print (a)

desde = 1
hasta = 50
b = validarEnteroRango("Ingrese un valor entre 1 y 50: ",desde,hasta)
print(b)