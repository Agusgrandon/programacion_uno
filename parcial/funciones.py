'''
Instancia: Primer Examen Parcial
Apellido y nombre: agustina isabel grandon / FUNCIONES
Division: 313-1
Fecha: 11/06/2024
Asignatura: Programacion I
Instancia: Primer Examen Parcial
'''
import json
#A
def cargar_json(nombre_archivo, key):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    return(data[key])

def len_funcion(variable:str)->int:
    contador = 0
    for letra in variable:
        contador  = contador + 1

    return contador

def capitalizar (variable:str):
    cantidad = len_funcion(variable)
    if ord(variable[0]) >= 97 and ord(variable[0]) <= 122:
        for i in range (cantidad):
            if i == 0 :
                inicial = chr(ord(variable[i])-32)
                #print(inicial) 
                retorno = inicial
            else:
                retorno += variable[i]
    else:
        retorno = variable
    return retorno

def convertir_mayuscula (variable:str):
    cantidad = len_funcion(variable)
    mayuscula = ''
    for i in range (cantidad):
        if ord(variable[i]) >= 97 and ord(variable[i]) <= 122:
            letra = chr(ord(variable[i])-32)
            mayuscula += letra
        else:
            mayuscula += variable[i]
    
    return mayuscula

#B) Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)].
def alta_de_pasajeros(lista:list):
    pasajeros = {}

    id = input("Ingresa el identificado del vuelo:  ")
    id = int(id)
    while id < 1:
        id = input('Opción invalida, por favor ingresa un ID mayor a 1:  ')
        id = int(id)

    #Aerolínea (AA, LATAM o IBERIA)
    aerolinea = input("Ingresa la aerolinea en la que viajas: AA, LATAM, IBERIA:  ")
    aerolinea = convertir_mayuscula(aerolinea)
    while aerolinea != "AA" and aerolinea != "LATAM" and aerolinea != "IBERIA":
        aerolinea = input("Error, reingresa la aerolinea en la que viajas: AA, LATAM, IBERIA:  ")
        aerolinea = convertir_mayuscula(aerolinea)

    #Apellido_Nombre_Pasajero (Hasta de 30 caracteres)
    apellido_y_nombre = input("Ingresa tu nombre y apellido:  ")
    caracteres = len_funcion(apellido_y_nombre)
    while caracteres > 30:
        apellido_y_nombre = input("Tu nombre no puede superar los 30 digitos, reingresalo:  ")
        caracteres = len_funcion(apellido_y_nombre)
    
    #DNI (número)
    dni = input("Ingresa tu dni:  ")
    dni = int(dni)
    while dni > 60000000:
        dni = input('Error, por favor reingresa tu DNI:  ')
        dni = int(dni)

    #Precio (Entre 500.000 y 2.000.000)
    precio = input("Selecciona el precio entre 500.000 y 2.000.000:  ")
    precio = int(precio)
    while precio < 500000 or precio > 2000000:
        precio = input("Error, selecciona el precio:  ")
        precio = int(precio)

    #Origen (Buenos Aires, Madrid, París, Miami, Roma o Tokio)
    origen = input("Ingresa desde donde viajas (Buenos Aires, Madrid, París, Miami, Roma o Tokio):  ")
    origen = capitalizar(origen)
    while origen != "Buenos aires" and origen != "Madrid" and origen != "Paris" and origen != "Miami" and origen != "Roma" and origen != "Tokio":
        origen = input("Error, ingresa desde donde viajas:  ")
        origen = capitalizar(origen)

    #Destino (Buenos Aires, Madrid, París, Miami, Roma o Tokio)
    destino = input("Ingresa tu destino (Buenos Aires, Madrid, París, Miami, Roma o Tokio):  ")
    destino = capitalizar(destino)
    while destino != "Buenos aires" and destino != "Madrid" and destino != "Paris" and destino != "Miami" and destino != "Roma" and destino != "Tokio":
        destino = input("Error, reingresa tu destino:  ")
        destino = capitalizar(destino)

    #Clase (Turista o Ejecutivo)
    clase = input("Selecciona la clase (Turista o Ejecutivo):  ")
    clase = capitalizar(clase)
    while clase != "Turista" and clase != "Ejecutivo":
        clase = input("Error, selecciona la clase:  ")
        clase = capitalizar(clase)

    #Fecha (formato AAAAMMDD)
    fecha = input("Ingresa la fecha en la que viajas (formato AAAAMMDD):  ")
    fecha = int(fecha)
    while fecha < 20240610 or fecha > 20250131:
        fecha = input('La fecha ingresa no es correcta, reingresala:  ')
        fecha = int(fecha)

    
    pasajeros['Id'] = id
    pasajeros['Aerolinea'] = aerolinea
    pasajeros['Apellido_Nombre_Pasajero'] = apellido_y_nombre
    pasajeros['DNI_Pasajero'] = dni
    pasajeros['Precio'] = precio
    pasajeros['Origen'] = origen
    pasajeros['Destino'] = destino
    pasajeros['Clase'] = clase
    pasajeros['Fecha'] = fecha

    lista.append(pasajeros)

    return lista

#E – Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera: Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre
def listar_lista_de_pasajes(lista:list):

    print("Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre")
    for datos in lista:
        mensaje = f"{datos['Fecha']} | {datos['Aerolinea']} | {datos['Clase']} | {datos['Origen']} | {datos['Destino']} | {datos['Precio']} | {datos['DNI_Pasajero']} | {datos['Apellido_Nombre_Pasajero']}"
        print(mensaje)

#C – Modificar datos: Listar id y nombre de todos los pasajes, luego buscarlo por id y realizar la  modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese id,  tipo y dato a modificar”).
def validar_respuesta(rta:str)-> bool: 
    retorno = False
    if rta == "S" or rta == "s" or rta=="N" or rta == "n":
        retorno = True
    return retorno

def modificar_datos(lista:list):
    for pasaje in lista:
        mensaje = f"El identificador de ID es: {pasaje['Id']}, y el nombre del pasajero es: {pasaje['Apellido_Nombre_Pasajero']}"
        print(mensaje)

    id_a_buscar = input('Ingresa el identificador de ID:  ')
    id_a_buscar = int(id_a_buscar)

    for pasajes in lista:
        if pasajes['Id'] == id_a_buscar:
            print(f"Dato encontrado, el ID a modificar es: {id_a_buscar}.\n")
            modificar = input(f"Seleccione la opcion que desee modificar:  \n"
                f"1) El DNI, apellido y nombre: \n"
                f"2) Fecha: \n")
            match modificar:
                case '1':
                    dni = input('Ingresa el dni: ')
                    dni = int(dni)
                    while dni > 60000000:
                        dni = input('Error, por favor reingresa tu DNI:  ')
                        dni = int(dni)
                    apellido_y_nombre = input("Ingresa tu nombre y apellido:  ")
                    caracteres = len(apellido_y_nombre)
                    while caracteres > 30:
                        apellido_y_nombre = input("Tu nombre no puede superar los 30 digitos, reingresalo:  ")
                        caracteres = len(apellido_y_nombre)
                    confirmar = input("Desea modificar [S | N]?")
                    while validar_respuesta(confirmar)== False:
                        confirmar = input("Desea modificar [S | N]?")
                    if confirmar == "S" or confirmar == "s":    
                        pasajes['DNI_Pasajero'] = dni
                        pasajes['Apellido_Nombre_Pasajero'] = apellido_y_nombre
                        print('¡Datos modificados con exito!')
                    else:
                        print("El dato no se ha modificado")
                case '2':
                    fecha = input('Ingresa tu nueva fecha de viaje:  ')
                    fecha = int(fecha)
                    while fecha < 20240610 or fecha > 20250131:
                        fecha = input('La fecha ingresada no es correcta, reingresala:  ')
                        fecha = int(fecha)
                    confirmar = input("Desea modificar [S | N]?")
                    while validar_respuesta(confirmar)== False:
                        confirmar = input("Desea modificar [S | N]?")
                    if confirmar == "S" or confirmar == "s":
                        pasajes['Fecha'] = fecha
                        print('¡Datos modificados con exito!')
                    else: 
                        print('Los datos no fueron modificados')

    return lista

#D – Borrar datos: Listar id y nombre de todos los pasajes, luego buscarlo por id y realizar la baja correspondiente.
def baja_de_pasajero(lista:list):
    for pasaje in lista:
        print('------------------------------------------------------------------------------')
        mensaje = f"El identificador de ID es: {pasaje['Id']}, y el nombre del pasajero es: {pasaje['Apellido_Nombre_Pasajero']}"
        print(mensaje)

    id_a_buscar = input('Ingresa el identificador de ID:  ')
    id_a_buscar = int(id_a_buscar)

    for pasajes in lista:
        if pasajes['Id'] == id_a_buscar:
            print(f"Dato encontrado, la baja a realizar es la del pasajero: {pasajes['Apellido_Nombre_Pasajero']}.\n")
            baja = input(f"¿Estas seguro que queres darlo de baja?:  \n"
                f"1) Si \n"
                f"2) No \n")
            match baja:
                case '1': 
                    pasajes['Id'] = id_a_buscar
                    pasajes['Aerolinea'] = ''
                    pasajes['Apellido_Nombre_Pasajero'] = ''
                    pasajes['DNI_Pasajero'] = ''
                    pasajes['Precio'] = ''
                    pasajes['Origen'] = ''
                    pasajes['Destino'] = ''
                    pasajes['Clase'] = ''
                    pasajes['Fecha'] = ''
                    confirmar = input("Desea modificar [S | N]?")
                    while validar_respuesta(confirmar)== False:
                        confirmar = input("Desea modificar [S | N]?")
                    if confirmar == "S" or confirmar == "s":    
                        print('¡Dato dado de baja con exito!')
                    else:
                        print("El dato no se dio de baja")
                case '2':
                    print("El dato no se dio de baja")
    
    return lista

#1) Listar por pantalla los pasajes de menor y mayor precio.
def calcular_pasaje_barato_y_caro(lista:list):

    bandera_pasaje_mas_caro = True
    bandera_pasaje_mas_barato = True

    for pasajes in lista:
        if bandera_pasaje_mas_caro == True or float(pasajes['Precio']) > pasaje_mas_caro:
            pasaje_mas_caro = float(pasajes['Precio'])
            precio_del_pasaje_max = pasajes['Precio']
            nombre_del_pasajero_max = pasajes['Apellido_Nombre_Pasajero']
            bandera_pasaje_mas_caro = False
        if bandera_pasaje_mas_barato == True or float(pasajes['Precio']) < pasaje_mas_barato:
            pasaje_mas_barato = float(pasajes['Precio'])
            precio_del_pasaje_min = pasajes['Precio']
            nombre_del_pasajero_min = pasajes['Apellido_Nombre_Pasajero']
            bandera_pasaje_mas_barato = False
    
    print("Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre")
    mensaje = (f"{pasajes['Fecha']} | {pasajes['Aerolinea']} | {pasajes['Clase']} | {pasajes['Origen']} | {pasajes['Destino']} | {precio_del_pasaje_min} | {pasajes['DNI_Pasajero']} | {nombre_del_pasajero_min}.\n"
                f"{pasajes['Fecha']} | {pasajes['Aerolinea']} | {pasajes['Clase']} | {pasajes['Origen']} | {pasajes['Destino']} | {precio_del_pasaje_max} | {pasajes['DNI_Pasajero']} | {nombre_del_pasajero_max}")
    return mensaje

#2) Calcular y mostrar la cantidad de pasajes de un destino determinado, el mismo será ingresado por el usuario por consola.
def calcular_destinos(lista:list):
    contador_roma = 0
    contador_paris = 0
    contador_bs_as = 0
    contador_madrid = 0
    contador_miami = 0
    contador_tokio = 0

    for lugares in lista:
        if lugares['Destino'] == 'Buenos Aires':
            contador_bs_as += 1
        elif lugares['Destino'] == 'Madrid':
            contador_madrid += 1
        elif lugares['Destino'] == 'Paris':
            contador_paris += 1
        elif lugares['Destino'] == 'Miami':
            contador_miami += 1
        elif lugares['Destino'] == 'Roma':
            contador_roma += 1
        else:
            contador_tokio += 1

    elegir_destino = input('Elegi el destino:  ')

    match elegir_destino:
        case 'Roma':
            mensaje = f"La cantidad de vuelos a Roma son: {contador_roma}"
        case 'Buenos aires':
            mensaje = f"La cantidad de vuelos a Buenos Aires son: {contador_bs_as}"
        case 'Madrid':
            mensaje = f"La cantidad de vuelos a Madrid son: {contador_madrid}"
        case 'Paris':
            mensaje = f"La cantidad de vuelos a Paris son: {contador_paris}"
        case 'Miami':
            mensaje = f"La cantidad de vuelos a Miami son: {contador_miami}"
        case 'Tokio':
            mensaje = f"La cantidad de vuelos a Tokio son: {contador_tokio}"
    return mensaje
'''
Corrección:

def calcular_destinos(lista):

contador = 0
elegir_destino = input('Elegi el destino:  ')

for lugares in lista:
    if lugares == elegir_destino:
        contador += 1
mensaje = f"La cantidad de vuelos a {elegir_destino} son {contador}"
return mensaje
'''

#3) Listar los pasajes ordenados por Fecha. Preguntar al usuario si lo quiere ordenar de manera ascendente(‘asc’) o descendente („desc‟). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble sort (burbujeo).
def swap(lista, indice_uno, indice_dos):
    auxiliar = lista[indice_uno]
    lista[indice_uno] = lista[indice_dos]
    lista[indice_dos] = auxiliar
    
    return lista

def ordenar_ascendente(lista:list, clave)-> list: 
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][clave] > lista[j][clave]:
                swap(lista, i, j)
    return lista

def ordenar_descendente(lista:list, clave)-> list: 
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][clave] < lista[j][clave]:
                swap(lista, i, j)
    return lista

#4) Exportar a JSON la lista de pasajes, de acuerdo a la opción F 3.
def generar_json(nombre:str, lista:list, clave:str):
    data = {clave:lista}
    with open (nombre, 'w') as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)

#5) Exportar a CSV la lista de pasajes, de acuerdo a la opción F 1.
def guardar_archivo(archivo_nombre:str, contenido_archivo:str):
    if len(contenido_archivo) == 0:
        retorno = False
    else:
        with open(archivo_nombre, 'w+') as archivo:
            archivo.write(contenido_archivo)
        retorno = f"Se creó el archivo: {archivo_nombre}"
    return retorno

def generar_csv(nombre_csv:str, lista:list):
    if len(lista) == 0:
        retorno = False
    else:
        claves = ""
        datos = ""
        for key in lista[0].keys():
            claves += key + ","
        claves += '\n'
        for personaje in lista:
            for dato in personaje.values():
                datos += str(dato) + ","
            datos += '\n'
        guardar_archivo(nombre_csv, claves + datos)