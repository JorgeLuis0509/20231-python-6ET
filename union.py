from csv import list_dialects
from urllib import response
lista1 = input("Numero de la lista 1 : ")
lista2 = input("Numero de la lista 1 : ")
lista3 = input("Numero de la lista 1 : ")
lista4 = input("Numero de la lista 1 : ")
lista5 = input("Numero de la lista 1 : ")
lista6 = input("Numero de la lista 1 : ")

lista10 = input("Numero de la lista 2 : ")
lista11 = input("Numero de la lista 2 : ")
lista12 = input("Numero de la lista 2 : ")

union1=[]
union1.insert(0,lista1)
union1.insert(1,lista2)
union1.insert(2,lista3)
union1.insert(3,lista4)
union1.insert(4,lista5)
union1.insert(5,lista6)


union2=[]
union2.insert(0,lista10)
union2.insert(1,lista11)
union2.insert(2,lista12)

def leerLista():
    union1 =[]
    union2=[]
    response =[[],[]]
    for x in range(5):
        union1.append(int(input("Ingrese datos para la lista Uno: ")))
    print("*****************************")
    for y in range(4):
        union2.append(int(input("Ingrese datos de la lista Dos: ")))
        response[0]=union1
def menu():
  print("***OPERACIONES CON LISTAS***")
  print("0- Salir ")
  print("1- Leer las dos listas ")
  print("2- Union")
  print("3- Diferencia ")
  print("4- Diferencia simetrica")
  print("5- Invertirseccion")
  print("6- Invertir orden de elementos ***")
menu()
def leerEntero(mensaje):
  flag = True
  while flag:
    try:
      num = int(input(mensaje))
      flag = False
    except ValueError:
      print("Error: Debe ingresar un entero valido.")
  return num
opcion = 1
flag = True


while ( flag ):
  opcion = leerEntero("Ingrese opcion: ")
  match opcion:
    case 0:
        print("Adios ")
        flag = False
    case 1:
        print(union1)
        print(union2)
        menu()       
    case 2:
        print("Union de las dos listas: ", set(union1) | set(union2))
        menu()
    case 3:
        print("La diferencia simetrica es: ", set(union1) - set(union2))
        menu()
    case 4:
        print("La interacion es: ", set(union1) ^ set(union2))
        menu()
    case 5:
        print("La interceccion es: ", set(union1) & set(union2))
        menu()
    case 6:
        listainvertida= union1
        listainvertida.reverse()
        print(f"Datos de la lista uno {union1} Lista uno invertida: {listainvertida}")