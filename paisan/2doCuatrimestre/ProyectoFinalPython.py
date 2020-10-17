
def newUser():
    f = open("infoEmpleados.txt", "a")
    idEmployee= input("Ingrese el numero de legajo del empleado: ")
    nameEmployee= input("Ingrese el nombre del empleado: ")
    salaryEmployee= input("Ingrese el salario bruto del empleado: ")
    data = idEmployee+nameEmployee.center(20)+"$"+salaryEmployee.center(10)+"\n"
    f.write(str(data))
    f.close()

def removeUser():
    f = open("infoEmpleados.txt", "r+")
    listEmployeeId= f.readlines()
    employeeId= input(str("Ingrese el numero de legajo del empleado a dar de baja: "))
    warning= print("\nUsted ingresó el legajo", employeeId,". Está seguro de dar de baja este legajo? \nESTA ACCION NO SE PUEDE DESHACER")
    confirmation = input("S/N\n")
    if ( confirmation == "S"):
        
        idRemoved = 0
        for line in listEmployeeId:
            result = (line[:3])
            if (result == employeeId):
            # if result!=employeeId:
                # f.seek(0)
                listEmployeeId.remove(line)
                # f.write(line)
                idRemoved = 1
            elif result!=employeeId:
                f.write(line)
        if (idRemoved == 1):
            print("El legajo",employeeId,"fue eliminado satisfactoriamente.")
        else:
            print("El legajo",employeeId,"no existe.")
    for line in listEmployeeId:
        print (line)
    f.close()
    # elif (estaSeguro.upper() == "N"):


removeUser()

# for line in lines:
#      if line!=result+"\n":
#        f.write(line)