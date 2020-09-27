nombreEmpleado = str(input("Ingrese el nombre del empleado: "))
salario = float(input("Ingrese el monto de su salario: "))
aumento = float(input("Ingrese el porcentaje de aumento: "))

diferenciaSalario = salario * aumento / 100
salarioAjustado = diferenciaSalario + salario

print("El emepleado ",nombreEmpleado,"percibirá un aumento de $",diferenciaSalario,"en su salario.")
print("Su nuevo salario será de $",salarioAjustado)