import shutil
import os

def createFile():
    if os.path.isfile("infoEmpleados.txt"):
        print("\nEl archivo ya existe.\n")
    else:
        fileToEdit = open("infoEmpleados.txt","w")
        headers = ("{0:<10} {1:<15} {2:<10} \n".format("LEGAJO", "NOMBRE", "SALARIO"))
        fileToEdit.write(headers)
        if os.path.isfile("infoEmpleados.txt"):
            print("\nArchivo creado.\n")
        else:
            print("\nError al crear el archivo.\n")

def newUser():
    if os.path.isfile("infoEmpleados.txt"):
        f = open("infoEmpleados.txt", "a")
        idEmployee= input("Ingrese el numero de legajo del empleado en formato de 3 números. Ejemplo 002: ")
        nameEmployee= input("Ingrese el nombre del empleado: ")
        salaryEmployee= input("Ingrese el salario bruto del empleado: ")
        # data = idEmployee+"     "+nameEmployee+"     $"+salaryEmployee+"\n"
        data = ("{0:<10} {1:<15} ${2:<10} \n".format(idEmployee, nameEmployee, salaryEmployee))
        f.write(str(data))
        f.close()
    else:
        print("El archivo no existe. Por faorutilice la opción 1 para crearlo.")

def removeUser():
    f = open("infoEmpleados.txt", "r+")
    listEmployeeId= f.readlines()
    employeeId= input(str("Ingrese el numero de legajo del empleado a dar de baja: "))
    print("\nUsted ingresó el legajo", employeeId,". Está seguro de dar de baja este legajo? \nESTA ACCION NO SE PUEDE DESHACER")
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

def updateUser():
    f = open("infoEmpleados.txt", "r+")
    listEmployeeId= f.readlines()
    employeeId= input(str("Ingrese el numero de legajo para modificar su salario: "))
    print("\nUsted ingresó el legajo", employeeId,". Está seguro que desea modificar este legajo? \nESTA ACCION NO SE PUEDE DESHACER")
    confirmation = input("S/N\n")
    newSalaryEmployee= input("Ingrese el nuevo salario bruto del empleado: ")
    if (confirmation == "S"):
        f.seek(0)
        idRemoved = 0
        for line in listEmployeeId:
            result = (line[:3])
            if (result == employeeId):
                employeeName = (line[11:22])
                listEmployeeId.remove(line)
                idRemoved = 1
            elif result!=employeeId:
                f.write(line)
        if (idRemoved == 1):
            print("El legajo",employeeId,"fue modificado satisfactoriamente.")
        else:
            print("El legajo",employeeId,"no existe.")
    elif (confirmation == "N"):
        print("\nComando cancelado.\n")
    f.close()
    shutil.move("infoEmpleados.txt","infoEmpleados.old")
    f = open("infoEmpleados.txt", "w")
    f.writelines(listEmployeeId)
    f.close() 
    f = open("infoEmpleados.txt", "a")
    f.write("{0:<10} {1:<15} ${2:<10} \n".format(employeeId, employeeName, newSalaryEmployee))
    f.close()
    # f = open("./infoEmpleados.txt", "r+")
    # listEmployeeId= f.readlines()
    # print(listEmployeeId)
    # for i in sorted(listEmployeeId):
    #     f.write(i)
    #     listEmployeeId.remove(i)
    #     print(i)
    # f.close()


# createFile()

# print ("Crear usuario")
# newUser()
# # newUser()
# # newUser()
# print("")
# print ("Borrar usuario")
# removeUser()
# print("")
# print ("Modificar usuario")
updateUser()