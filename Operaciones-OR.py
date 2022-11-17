def menu():
    print (""" OPERACIONES CON LISTAS 
    0- Salir" 
    1- Leer las 2 litas"
    2- Union"
    3- Diferencia"
    4- Diferencia simetrica"
    5- Interseccion"
    6- Invertir orden de elementos """)


def Datos(mensaje):
  flag = True
  while flag:
    try:
      num = int(input(mensaje))
      flag = False
    except ValueError:
      print("Error: Debe ingresar un entero válido.")
  return num

def leerlistas():
  lista1 =[0]
  lista2 =[1]
  response = [[],[]]
  for x in range (5):
    lista1.append(int(input("Ingresae datos para la lista uno: ")))
  print("*"* 50)
  for y in range (4):
    lista2.append(int(input("Ingresae datos para la lista dos: ")))
    print ("*"* 50)
  response[0]= lista1
  response[1] = lista2
  return response

from importlib import * 
datos = leerlistas()
lista1 = datos[0]
lista2 = datos[1]

while True:
  menu()
  opcion = int(input("ingresar una opcion>>"))
  if opcion == 0:
    print("y :")
 #   break 
  if opcion == 1:
    print(f"lista uno: {lista1} /n lista dos:  {lista2}")
  if opcion == 2:
    print("Union de las dos listas: ", set(lista1) | set(lista2))
  if opcion == 3:
    print("la diferencia es: ", set(lista1) - set(lista2))
  if opcion == 4:
    print("la diferencia simetrica es: ", set(lista1) ^ set(lista2))
  if opcion == 5:
   print("La interación es: ", set(lista1) & set(lista2))
  if opcion == 6:
   listIn  = lista1
   listIn.reverse()
   print(f"datos de la lista uno {lista1} datos de la lista invertida: {listIn}")
   listIn2  = lista2
   listIn2.reverse()
   print(f"datos de la lista dos {lista2} datos de la lista invertida: {listIn2}")

