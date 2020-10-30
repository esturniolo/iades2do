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

def showUsers():
    if os.path.isfile("infoEmpleados.txt"):
        f = open("infoEmpleados.txt", "r")
        f.seek(39)
        showEmployeesSorted = f.readlines()
        f.close()
        print("{0:<10} {1:<15} {2:<10} \n".format("LEGAJO", "NOMBRE", "SALARIO"))
        for ele in sorted(showEmployeesSorted): 
            print(ele)
    else:
        print("El archivo no existe. Por favor utilice la opción 1 para crearlo.")

def newUser():
    if os.path.isfile("infoEmpleados.txt"):
        f = open('infoEmpleados.txt', "r")
        lines = f.read().splitlines()
        lastLine = lines[-1]
        f.close()
        substring="LEGAJO"
        f = open("infoEmpleados.txt", "a")
        if (lastLine.find(substring) != -1):
            print("No hay ningún usuario en la lista.")
        else: 
            # print("El último usuario en la lista es:\n", lastLine,"\n")
            print("\n                   *-*-*-* IMPORTANTE *-*-*-*\n\nSi tiene dudas con el último usuario ingresado, por favor revise este dato con la \nopción 6 'Listar Usuarios' para evitar usuarios duplicados.\n")
            print("Desea revisar esta opción ahora?")
            check6 = input("S/N\n")
            if (check6=="S"):
                os.system('clear')
                showUsers()
                print("\n")
        idEmployee= input("Ingrese el numero de legajo del empleado en formato de 3 números. Ejemplo 001: ")
        nameEmployee= input("Ingrese el nombre del empleado: ")
        salaryEmployee= input("Ingrese el salario bruto del empleado: ")
        # data = idEmployee+"     "+nameEmployee+"     $"+salaryEmployee+"\n"
        data = ("{0:<10} {1:<15} ${2:<10} \n".format(idEmployee, nameEmployee, salaryEmployee))
        f.write(str(data))
        f.close()
    else:
        print("El archivo no existe. Por favor utilice la opción 1 para crearlo.")

def removeUser():
    if os.path.isfile("infoEmpleados.txt"):
        f = open("infoEmpleados.txt", "r+")
        listEmployeeId= f.readlines()
        employeeId= input(str("Ingrese el numero de legajo del empleado a dar de baja: "))
        print("\nUsted ingresó el legajo", employeeId,". Está seguro de dar de baja este legajo? \nESTA ACCION NO SE PUEDE DESHACER")
        confirmation = input("S/N\n")
        if (confirmation.upper() == "S"):
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
        elif (confirmation.upper() == "N"):
            print("\nComando cancelado.")
            input("\nPresione una tecla para continuar...")
        f.close()
        shutil.move("infoEmpleados.txt","infoEmpleados.tmp")
        f = open("infoEmpleados.txt", "w")
        f.writelines(listEmployeeId)
        f.close()
    else:
         print("El archivo no existe. Por favor utilice la opción 1 para crearlo.")

def updateNameUser():
    if os.path.isfile("infoEmpleados.txt"):
        f = open("infoEmpleados.txt", "r+")
        listEmployeeId= f.readlines()
        employeeId= input(str("Ingrese el numero de legajo para modificar su nombre: "))
        print("\nUsted ingresó el legajo", employeeId,". Está seguro que desea modificar este legajo? \nESTA ACCION NO SE PUEDE DESHACER")
        confirmation = input("S/N\n")
        newNameEmployee= input("Ingrese el nuevo nombre del empleado: ")
        employeeSalary="0"
        if (confirmation.upper().upper() == "S"):
            f.seek(0)
            idRemoved = 0
            for line in listEmployeeId:
                result = (line[:3])
                if (result == employeeId):
                    employeeSalary = (line[28:39])
                    listEmployeeId.remove(line)
                    idRemoved = 1
                elif result!=employeeId:
                    f.write(line)
            if (idRemoved == 1):
                print("El legajo",employeeId,"fue modificado satisfactoriamente.")
            else:
                print("El legajo",employeeId,"no existe.")
        elif (confirmation.upper() == "N"):
            print("\nComando cancelado.")
            input("\nPresione una tecla para continuar...")
            cancel = 1
        if (cancel!=1):
            f.close()
            shutil.move("infoEmpleados.txt","infoEmpleados.tmp")
            f = open("infoEmpleados.txt", "w")
            f.writelines(listEmployeeId)
            f.close() 
            f = open("infoEmpleados.txt", "a")
            f.write("{0:<10} {1:<15} ${2:<10} \n".format(employeeId, newNameEmployee, employeeSalary))
    else:
         print("El archivo no existe. Por favor utilice la opción 1 para crearlo.")

def updateSalaryUser():
    if os.path.isfile("infoEmpleados.txt"):
        f = open("infoEmpleados.txt", "r+")
        listEmployeeId= f.readlines()
        employeeId= input(str("Ingrese el numero de legajo para modificar su salario: "))
        print("\nUsted ingresó el legajo", employeeId,". Está seguro que desea modificar este legajo? \nESTA ACCION NO SE PUEDE DESHACER")
        confirmation = input("S/N\n")
        newSalaryEmployee= input("Ingrese el nuevo salario bruto del empleado: ")
        employeeName=""
        if (confirmation.upper() == "S"):
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
        elif (confirmation.upper() == "N"):
            print("\nComando cancelado.")
            input("\nPresione una tecla para continuar...")
            cancel = 1
        if (cancel!=1):
            f.close()
            shutil.move("infoEmpleados.txt","infoEmpleados.tmp")
            f = open("infoEmpleados.txt", "w")
            f.writelines(listEmployeeId)
            f.close() 
            f = open("infoEmpleados.txt", "a")
            f.write("{0:<10} {1:<15} ${2:<10} \n".format(employeeId, employeeName, newSalaryEmployee))
            f.close()
    else:
        print("El archivo no existe. Por favor utilice la opción 1 para crearlo.")

def backup():
    if os.path.isfile("infoEmpleados.txt"):
        myPath = input("Ingrese el path completo (Ej C:\directorioBackUp) de donde quiere hacer su backup. Si el directorio no existe, el programa lo creará por usted: ")
        if not os.path.isdir(myPath):
            os.makedirs(myPath)
        shutil.copy("infoEmpleados.txt", myPath)
        os.remove("infoEmpleados.tmp")
    else:
        print("El archivo no existe. Por favor utilice la opción 1 para crearlo.")

def menu():
    while True:
        os.system('clear')
        print(30 * "-", "Trabajo Final Emiliano Sturniolo - Analista 2020 - IADES", 30 * "-")
        print("\nIngrese la opción deseada:")
        print("-------------------------")
        print("1. Crear archivo de empleados.")
        print("2. Ingresar nuevo empleado.")
        print("3. Borrar empleado existente.")
        print("4. Modificar nombre de usuario existente.")
        print("5. Modificar salario de usuario existente.")
        print("6. Listar usuarios.")
        print("7. Realizar backup y borrar archivos temporales.")
        print("8. Salir.")
        print(118 * "-")
        print("")
        bye = input("Su opción: ")
        print("\n")

        if (bye=='1'):
            createFile()
            input("\nPresione una tecla para continuar...")
        elif (bye=='2'):
            newUser()
            input("\nPresione una tecla para continuar...")
        elif (bye=='3'):
            removeUser()
            input("\nPresione una tecla para continuar...")
        elif (bye=='4'):
            updateNameUser()
            input("\nPresione una tecla para continuar...")
        elif (bye=='5'):
            updateSalaryUser()
            input("\nPresione una tecla para continuar...")
        elif (bye=='6'):
            showUsers()
            input("\nPresione una tecla para continuar...")
        elif (bye=='7'):
            backup()
            input("\nPresione una tecla para continuar...")
        elif (bye=='8'):
            print("\nGracias por utilizar este software.\n")
            break

menu()
