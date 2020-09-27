salarioPorHoraDocente = 480
descJubilacion = 11
descObraSocial = 3
horasCatedra = 23

bruto = salarioPorHoraDocente * horasCatedra
neto = bruto - (bruto * descJubilacion / 100) - (bruto * descObraSocial / 100)

print("Salario bruto $",bruto)
print("Salario neto $",neto)
