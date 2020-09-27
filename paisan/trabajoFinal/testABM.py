#segovia-altas-bajas-sqlite3


import sqlite3 as dbapi
import os
arch="bbdd.dat"



def AgregaDatoDeptos():  #Agrega datos a la tabla deptos si el depto coincide con alguno de personas imprime la direccion
 bbdd = dbapi.connect(arch)
 cursor = bbdd.cursor()
 print('Ingrese el Depto')
 dep=raw_input('Depto: ');
 while (dep!='0'):
  dire=raw_input('Direccion: ');
  cursor.execute("insert into Deptos values (?,?)",(dep,dire))#Recordar que es posicional los ?
  print('Ingrese otro depto, o cero para salir');
  dep=raw_input('Depto: ');
  bbdd.commit()
 bbdd.close()


def AgregaDatoPersonas():  #Agrega datos a la tabla personas
 bbdd = dbapi.connect(arch)
 cursor = bbdd.cursor()
 print('Ingrese el nombre')
 nom=raw_input('Nombre: ');
 while (nom!='0'):
  doc=raw_input('Doc: ');
  departamento=raw_input('Departamento: ');
  cursor.execute("insert into Personas values (?,?,?)",(nom,doc,departamento))#Recordar que es posicional los ?
  print('Ingrese otro nombre, o cero para salir');
  nom=raw_input('Nombre: ');
  bbdd.commit()
 bbdd.close()


def CrearTabla(): #Crea Tablas solo si no existen
  bbdd = dbapi.connect(arch)
  cursor = bbdd.cursor()
  cursor.execute("""create table if not exists Personas (Id INTEGER UNIKE PRIMARY KEY, nombre text,dni text,departamento text)""")
  cursor.execute("""create table if not exists Deptos (Id INTEGER UNIKE PRIMARY KEY, Depto text,Direccion text)""")
  bbdd.commit()
  bbdd.close()


def Modificar(): #Modifica datos de  una persona buscada por nombre
  nom2=raw_input("Ingrese el nombre a buscar: ")
  nom=raw_input('Nombre modificado: ');
  doc=raw_input('Doc modificado: ');
  dep=raw_input('Departamento modificado: ');
  bbdd = dbapi.connect(arch)
  cursor = bbdd.cursor()
  cursor.execute("UPDATE Personas SET nombre = '"+nom+"',dni = '"+doc+"',departamento = '"+dep+"' WHERE nombre = '"+nom2+"'")
  nom2=raw_input("Desea guardar los cambios? responder con s o n ") #guarda o no los cambios recicle la variable jeje
  if nom2=='s':
   bbdd.commit()
  else:
   bbdd.rollback()
  bbdd.close()

def ImprimirDatos(): #Imprime la tabla ordenada por departamento
  if os.path.exists(arch):
   bbdd = dbapi.connect(arch)
   cursor = bbdd.cursor()
   cursor.execute("select * from Personas order by departamento")
   #print "Cantidad de elementos: "+str(len(cursor.fetchall()))  #cantidad de elementos al usarlo vacia la tupla
   print "Listado de Personas"
   print " "
   for tupla in cursor.fetchall():
    print tupla #En caso de querer imprimir solo un dato usar tupla[0] un rango tupla[0:1]
   print "------------------------------------------"
   print "Nombre de Campos"
   print " "
   cursor.execute("select * from Personas")
   for i in cursor.description:
    print i[0]

   #print cursor.description()
   #for tupla in cursor.fetchall():
   # print tupla
   bbdd.close()
  else:
   print "No existe el archivo"

def ImprimirTablasJuntas():
  bbdd = dbapi.connect(arch)
  cursor = bbdd.cursor()
  cursor.execute("select * from Personas,Deptos where Personas.departamento=Deptos.Depto")
  for tupla in cursor.fetchall():
   print tupla
  bbdd.close()

def ImprimirTablasCantporDepto():
  bbdd = dbapi.connect(arch)
  cursor = bbdd.cursor()
  #cursor.execute("select Personas.departamento,Deptos.Depto from Personas,Deptos Left Join Deptos USING(Depto)")
  cursor.execute("select distinct(Personas.departamento),count(Personas.departamento) from Personas group by departamento")
  for tupla in cursor.fetchall():
   print tupla
  bbdd.close()

def BorraDato(): #Borra una persona
  bbdd = dbapi.connect(arch)
  cursor = bbdd.cursor()
  nom=raw_input('Nombre: ')
  cursor.execute("DELETE from Personas WHERE nombre='"+nom+"'")
  bbdd.commit()
  bbdd.close()


if __name__=="__main__":
 op='2'
 while (op!='0'):
  print('\n*****************************')
  print('    Menu Principal   ')
  print('*****************************')
  print('0-Salir')
  print('1-Agregar Dato Personas')
  print('2-AgregarDepto')
  print('3-Modificar Dato')
  print('4-Borra Dato')
  print('5-Crear Tabla')
  print('6-Imprimir Tablas Juntas')
  print('7-Imprimir Tablas Cantidad por Depto')
  print('8-Imprimir Datos')
  print('*****************************')
  op=raw_input('Opcion: ')
  if (op=='1'):
      AgregaDatoPersonas()
  elif (op=='2'):
      AgregaDatoDeptos()
  elif (op=='3'):
      Modificar()
  elif (op=='4'):
      BorraDato()
  elif (op=='5'):
      CrearTabla()
  elif (op=='6'):
      ImprimirTablasJuntas()  
  elif (op=='7'): #Usa el  count
      ImprimirTablasCantporDepto()  
  elif (op=='8'):
      ImprimirDatos()
