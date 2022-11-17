from tkinter import N

def leerEntero(mensaje):
  flag = True
  while flag:
    try:
      num = int(input(mensaje))
      flag = False
    except ValueError:
      print("Error: Debe ingresar un entero valido.")
  return num
def submenu():
  print("1- Ingresar alumno 1",Alumno1)
  print("2- Ingresar alumno 2",Alumno2)
def menu():
  print("******  MENU  ******")
  print("0- Salir ")
  print("1- Ingresar nombre de 2 alumnos ")
  print("2- Ingresar notas ")
  print("3- Calcular promedio ")
  print("4- Mostrar registros")
  print(">>> Ingrese una opcion: ")
menu()
opcion = 1
flag = True
while ( flag ):
  opcion = leerEntero("Ingrese opcion: ")
  match opcion:
    case 0:
        print("Adios ")
        flag = False
    case 1:
        Alumno1 = input("Nombre del Alumno 1 : ")
        Alumno2 = input("Nombre del alumno 2 : ")
        menu()
    case 2:
        print("1- Ingresar alumno 1 ")
        print("2- Ingresar alumno 2 ")
        opcion1= int(input(">>> Ingrese una opcion:"))
        if(opcion1==1):
          print("**   Ingrese nota del alumno" , Alumno1)
          nota1= int(input("Ingrese Nota 1: "))
          nota2= int(input("Ingrese Nota 2: "))
          nota3= int(input("Ingrese Nota 3: "))
          menu()
        else: 
          if (opcion1==2):
            print("**   Ingrese nota del alumno" , Alumno2)
            nota1= int(input("Ingrese Nota 1: "))
            nota2= int(input("Ingrese Nota 2: "))
            nota3= int(input("Ingrese Nota 3: "))
        menu()
    case 3:
        promedio = (nota1 + nota2 + nota3)//3
        if promedio >=0 and promedio<= 10:
          resultado =("REPROBADO  ")
        elif promedio >= 10 and promedio < 13:
          resultado=("DESAPROBADO ")
        elif promedio >= 13 and promedio <=20:
          resultado=("APROBADO ")
        print("**LISTO**")
        menu()
    case 4:
      print(Alumno1,nota1, nota2,nota3,promedio, resultado)
      print( Alumno2,nota1,nota2, nota3, promedio, resultado)
      print ("ALUMNO "+'\t\t'+"Nota1"+'\t'+"nota2"+'\t'+"nota3"+'\t'+"Promedio"+"\t"+"Resultado")
      print (Alumno1,"\t\t",nota1,"\t",nota2,'\t',nota3,'\t',promedio,"\t\t",resultado)

 

