lado1 = float(input("Ingrese el valor del lado 1: "))
lado2 = float(input("Ingrese el valor del lado 2: "))
lado3 = float(input("Ingrese el valor del lado 3: "))
if(lado1==lado2 and lado2==lado3):
    print("El Triangulo es Equilatero")
elif(lado1==lado2 or lado1==lado3 or lado2==lado3):
    print ("El Triangulo es Isoceles")
elif (lado1!=lado2 or lado1!=lado3 or lado2!=lado3):
    print ("El Triangulo es Escaleno")