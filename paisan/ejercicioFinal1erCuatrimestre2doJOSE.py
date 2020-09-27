m=[["Provincia","Enero","Febrero","Marzo","Abril"],
["Buenos Aires",300,400,300,200],
["CABA",300,400,500,200],
["Santa Cruz",200,300,200,100],
["Cordoba",100,200,300,100]]

v=["Total de "]

for f in range(len(m)):
    print(m[f][0].ljust(12)," ",end="")
    for c in range(1,5):
        print(str(m[f][c]).rjust(8)," ",end="")
    print("")

print("---------------------------------------------------------")
print("")

while True:
    provincia=input("Ingresar provincia a actualizar (nombre): ")
    if provincia.upper() == "FIN":
        break
    for f in range(len(m)):
        if m[f][0] == provincia:
            numprov = f
            break
    mes=int(input("Mes a actualizar (numero de mes) :"))
    valor=int(input("Cantidad de casos a sumar: "))
    m[numprov][mes] = m[numprov][mes] + valor
    print("")

for f in range(1,len(m)):
    suma = 0
    for c in range (1,5):
        suma = suma + m[f][c]
        print("")
    v.append(suma)

for f in range (1,len(v)):
    print(''.join(v[0]),m[f][0]," ",v[f])