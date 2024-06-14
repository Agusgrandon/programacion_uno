'''
Instancia: Primer Examen Parcial
Apellido y nombre: AGUSTINA ISABEL GRANDON, MENU DE OPCIONES
Division: 313-1
Fecha: 11/06/2024
Asignatura: Programacion I
Instancia: Primer Examen Parcial
'''
from os import system 
from funciones import *

continuar = True

while continuar:
      
    print("a) Alta de datos\nb) Agregar un pasajero \nc) Modificar un pasajero\nd) Borrar un pasajero\ne) listar todos los pasajes\nf) Sub-menu\ng) Salir")
    ingresar_opcion = input("Ingresa una opcion:  ")
    system("cls")

    match ingresar_opcion: 
        case "A" | "a": 
            base_de_datos = cargar_json("data.json", "pasajeros")
        case "B" | "b":
            alta = alta_de_pasajeros(base_de_datos)
        case "C" | "c":
            modificar = modificar_datos(base_de_datos)
        case "D" | "d":
            baja = baja_de_pasajero(base_de_datos)
        case "E" | "e":
            listar = listar_lista_de_pasajes(base_de_datos)
        case "F" | "f":
                print("1)Listar por pantalla los pasajes de menor y mayor precio.\n2)Calcular y mostrar la cantidad de pasajes de un destino determinado\n3)Listar pasajes por fecha\n4)Exportar json\n5)Exportar csv")
                ingresar_opcion_dos = input("Ingresa una opcion:  ")

                match ingresar_opcion_dos:
                    case "1":
                        max_min = calcular_pasaje_barato_y_caro(base_de_datos)
                        print(max_min)
                    case "2":
                        destinos = calcular_destinos(base_de_datos)
                        print(destinos)
                    case "3":
                        elegir = input('¿Como queres ordenar: ASC o DESC? ')
                        if elegir == 'ASC':
                            ordenar_asc = ordenar_ascendente(base_de_datos, 'Fecha')
                            for datos in ordenar_asc:
                                mensaje = f"{datos['Fecha']} | {datos['Aerolinea']} | {datos['Clase']} | {datos['Origen']} | {datos['Destino']} | {datos['Precio']} | {datos['DNI_Pasajero']} | {datos['Apellido_Nombre_Pasajero']}"
                                print(mensaje)
                        else:
                            ordenar_des = ordenar_descendente(base_de_datos, 'Fecha')
                            for datos in ordenar_des:
                                mensaje = f"{datos['Fecha']} | {datos['Aerolinea']} | {datos['Clase']} | {datos['Origen']} | {datos['Destino']} | {datos['Precio']} | {datos['DNI_Pasajero']} | {datos['Apellido_Nombre_Pasajero']}"
                                print(mensaje)
                    case "4":
                        generar_archivo_json = generar_json('nueva_base_de_datos.json', base_de_datos, 'pasajeros')
                    case "5":
                        generar_csv = generar_csv('nuevo.csv', base_de_datos)
        case "G" | "g":
            continuar = False
        case _:
            print("La opcion ingresada no es correcta, intentelo nuevamente")