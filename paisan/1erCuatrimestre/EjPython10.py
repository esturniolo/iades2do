#!/usr/local/bin/python3

#Ejercicio de cálculo de notas de un alumno, tomando 3 notasy calculando determinado porcentaje de las mismas para hacer una nota final.

from decimal import Decimal
import os

os.system('cls')
os.system('clear')

print("")

nombreAlumno = str(input("Ingrese el nombre del alumno: "))
escrito = float(input("Ingrese la nota del exámen escrito: "))
oral = float(input("Ingrese ahora la nota del oral: "))
participacion = float(input("Por último por favor, ingrese la nota de la participación en clase: "))

escritoFinal = float(escrito*0.5)
oralFinal = float(oral*0.3)
participacionFinal = float(participacion*0.2)

print("")

print("La nota final de",nombreAlumno,"es:",round(escritoFinal+oralFinal+participacionFinal,2))

print("")