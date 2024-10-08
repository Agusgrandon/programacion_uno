'''
carga mixta, aleatoria y secuencial
'''
from os import system 
from funcion import *

nombres = ["A","A","A","A","A"]
estado = ["LIBRE","LIBRE","LIBRE","LIBRE","LIBRE"]
edad=["A","A","A","A","A"]
continuar = True


while continuar == True:
    
    print ("Menu")
    print ("1- alta")
    print ("2- listar")
    print ("3- baja")
    print ("4- modificar")
    print ("5- salir")

    opcion = input("Ingrese una opción")
    opcion = int(opcion)
    system("cls")

    match opcion:
        case 1:
            indice = buscar_libre(estado,"LIBRE")
            if indice >= 0:
                nombres[indice] = alta('Ingrese nombre: ')
                edad[indice] = alta('Ingrese edad: ')
                estado[indice] = "OCUPADO"
            else:
                print ("No se encontraron espacios disponibles")
                
        case 2:
            if lista_vacia(estado,"LIBRE") == False:
                listar(estado, nombres, edad)
            else:
                print("No hay datos para listar")
        case 3:
            if lista_vacia(estado, "LIBRE") == False:
                nombre_buscar = input ("Ingrese el nombre a buscar: ")
                indice = buscar(nombres,nombre_buscar)
                if indice >= 0:
                    print("Dato encontrado")
                    mostrar(nombres, edad, indice)
                    confirmar = input("Desea borrar [S | N]?")
                    while validar_respuesta(confirmar)== False:
                        confirmar = input("Desea borrar [S | N]?")
                    if confirmar == "S" or confirmar =="s":    
                        estado[indice] = "LIBRE"
                        print("El dato se ha eliminado")                            
                    else:
                        print("El dato no se ha eliminado")
                else:
                    print ("El nombre buscado no se encuentra en la lista")
            else:
                print("No hay datos para eliminar")
        case 4:
            if lista_vacia(estado, "LIBRE") == False:
                nombre_buscar = input ("Ingrese el nombre a buscar: ")
                indice = buscar(nombres,nombre_buscar)
                if indice >= 0:
                    print("Dato encontrado")
                    mostrar(nombres, edad, indice)
                    confirmar = input("Desea modificar [S | N]?")
                    while validar_respuesta(confirmar)== False:
                        confirmar = input("Desea modificar [S | N]?")
                    if confirmar == "S" or confirmar == "s":    
                        nombres[indice] = input("ingrese un nuevo nombre") 
                        print("El dato se ha modificado")                            
                    else:
                        print("El dato no se ha modificado")
                else:
                    print ("El nombre buscado no se encuentra en la lista")
            else:
                print("No hay datos para modificar")
        case 5:
            continuar = False
        case _:
            print ("La opción ingresada no es correcta")
