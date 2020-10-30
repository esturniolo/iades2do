def myName():
    print("-" * 27)
    print("Alumno: Emiliano Sturniolo")
    print("-" * 27)

def printMatrix(M):
    rows = len(M)
    columns = len(M[0])
    for i in range(rows):
        for j in range(columns):
            print("| {0} ".format(M[i][j]), sep=',', end='')
        print('|\n')

def maths(M):
    rows = len(M)
    excedente=40000
    for i in range(rows):
        if (M[i][1]>40000 and M[i][1]<80000):
            total=(M[i][1]-excedente)*10/100
            M[i][2] = total
        elif (M[i][1]>80000):
            total=(M[i][1]-excedente)*20/100
            M[i][2] = total

matrix=[["Bernasconi",50000,0],["Gutierrez ",35000,0],["Michalina ",75000,0],["Parodi",110000,0]]

myName()
maths(matrix)
printMatrix(matrix)
myName()