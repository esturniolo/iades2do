import shutil

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
    if (confirmation == "S"):
        f.seek(0)
        idRemoved = 0
        for line in listEmployeeId:
            result = (line[:3])
            if (result == employeeId):
                listEmployeeId.remove(line)
                idRemoved = 1
            elif result!=employeeId:
                f.write(line)
        if (idRemoved == 1):
            print("El legajo",employeeId,"fue eliminado satisfactoriamente.")
        else:
            print("El legajo",employeeId,"no existe.")
    elif (confirmation == "N"):
        print("\nComando cancelado.\n")
    for line in listEmployeeId:
        print (line)
    f.close()
    shutil.move("infoEmpleados.txt","infoEmpleados.old")
    f = open("infoEmpleados.txt", "w")
    f.writelines(listEmployeeId)
    f.close() 


removeUser()
