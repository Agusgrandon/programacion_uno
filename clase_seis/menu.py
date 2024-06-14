'''
carga mixta, aleatoria y secuencial
'''
nombres = ["A","A","A","A","A"]
continuar = True
contador = 0 
encontrado = False

while continuar == True:
    print ("Menu")
    print ("1- alta")
    print ("2- listar")
    print ("3- baja")
    print ("4- salir")

    opcion = input("Ingrese una opción")
    opcion = int(opcion)

    match opcion:
        case 1:
            if contador < len(nombres):
                for i in range(len(nombres)):
                    if nombres[i] == "A":
                        nombre = input("Ingrese un nombre: ")
                        nombres[i] = nombre
                        contador += 1
                        break
            else:
                print ("No se encontraron espacios disponibles")
                
        case 2:
            if contador > 0:
                for i in range(len(nombres)):
                    if nombres[i] != "A":
                        print(nombres[i])
            else:
                print("No hay datos para listar")
        case 3:
            if contador > 0:
                encontrado = False
                nombre_buscar = input ("Ingrese el nombre a buscar: ")
                for i in range(len(nombres)):
                    if nombre_buscar == nombres[i]:
                        nombres[i] = "A"
                        contador -= 1 
                        encontrado = True
                        break
                if encontrado == False:
                    print ("El nombre buscado no se encuentra en la lista")
            else:
                print("No hay datos para eliminar")
        case 4:
            continuar = False
        case _:
            print ("La opción ingresada no es correcta")