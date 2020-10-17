
def newUser():
    addEmployee= open("infoEmpleados.txt", "a")
    idEmployee= input("Ingrese el numero de legajo del empleado: ")
    nameEmployee= input("Ingrese el nombre del empleado: ")
    salaryEmployee= input("Ingrese el salario bruto del empleado: ")
    data = idEmployee+nameEmployee.center(20)+"$"+salaryEmployee.center(10)+"\n"
    addEmployee.write(str(data))
    addEmployee.close()

def removeUser():
    removeEmployee= open("infoEmpleados.txt", "r+")
    listEmployeeId= removeEmployee.readlines()
    employeeId= input(str("Ingrese el numero de legajo del empleado a dar de baja: "))
    warning= print("\nUsted ingresó el legajo", employeeId,". Está seguro de dar de baja este legajo? \nESTA ACCION NO SE PUEDE DESHACER")
    confirmation = input("S/N\n")
    if ( confirmation == "S"):
        # listEmployeeId= removeEmployee.readlines()
        # print (listEmployeeId)
        counter=0
        idRemoved = 0
        for line in listEmployeeId:
            result = (line[:3])
            if (result == employeeId):
                listEmployeeId.pop(counter)
                idRemoved = 1
            counter = counter + 1
        if (idRemoved == 1):
            print("El legajo",employeeId,"fue eliminado satisfactoriamente.")
        else:
            print("El legajo",employeeId,"no existe.")
    for line in listEmployeeId:
        print (line)
    removeEmployee.close()
    # elif (estaSeguro.upper() == "N"):


removeUser()

# removeEmployee= open("infoEmpleados.txt", "r+")
# listEmployeeId= removeEmployee.readlines()
# # print(listEmployeeId)

# print(listEmployeeId)

# a = str(111)
# contador=0

# for linea in listEmployeeId:
#     # print(linea)
#     resultado = (linea[:3])
#     if (resultado == a):
#         # print ("ok")
#         listEmployeeId.pop(contador)
#     # else:
#         # print ("notok")
#     contador = contador + 1

# print(listEmployeeId)
# removeEmployee.close()

# # a=111

# # for a in listEmployeeId

# # ['elementOne', 'elementThree']
# # >>> stringlist = [x for x in stringlist if "Two" not in x]
# # >>> stringlist
# # ['elementOne', 'elementThree']