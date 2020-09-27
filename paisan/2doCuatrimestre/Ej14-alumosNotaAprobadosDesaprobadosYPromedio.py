def Promedio(lista): 
    return sum(lista) / len(lista) 

nombreAlumno = ""
listaDesaprobados = []
listaAprobados = []

while True:
    nombreAlumno= str(input("Ingrese el nombre del alumno: "))
    if (nombreAlumno == "FIN"):
        break
    nota= float(input("Ingrese la nota final: "))
    print("")
    if (nota < 4):
        listaDesaprobados.append(nota)
    elif (nota >= 4):
        listaAprobados.append(nota)

try:
    promedioDesaprobados = Promedio(listaDesaprobados)
    print("El promedio de los reprobados es de",promedioDesaprobados)

except ZeroDivisionError:
    print("No hay alumnos reaprobados")
    
try:
    promedioAprobados = Promedio(listaAprobados)
    print("El promedio de los aprobados es de",promedioAprobados)
except ZeroDivisionError:
    print("No hay alumnos aprobados")



