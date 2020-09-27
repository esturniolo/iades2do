cantNumeros = 2
listaNumeros = [] 
  

for i in range (cantNumeros):
    nro = int(input("Ingrese un número:   "))
    listaNumeros.append(nro)

listaNumeros.sort() 

print("El numero mas grande es:", listaNumeros[-1]) 