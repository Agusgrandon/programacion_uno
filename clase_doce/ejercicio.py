'''
A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino
Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)
'''
from data_stark import lista_personajes

from os import system
from data_stark import lista_personajes
#from funciones import *

continuar = True


while continuar:

    print('\t A- Datos superheroe \n \tB- Identidad & Peso con mayor fueza \n \tC- SuperHeroe mas bajo \n \tD- peso promedio masculino \n \tE- Fuerza de superheroes mayores al promedio de fuerza femenino \n \t F-Salir ')

    opcion = input('Ingrese opcion:')

    system('cls')

    match opcion:
        case 'A' | 'a':
            system('cls')
            for datos in lista_personajes:
                for key_value in datos.items():
                    print(key_value[0],key_value[1])
                print('--------------------------')
        case 'B'  | 'b':
            '''B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)'''
            primera_fuerza = True
            for datos in lista_personajes:
                for key in datos.keys():
                    if key == 'fuerza':
                        if primera_fuerza == True or  int(datos[key]) > fuerza_maxima:
                            fuerza_maxima = int(datos[key])
                            identidad_maxima = datos['identidad']
                            peso_mayor_fuerza = datos['peso']
                            primera_fuerza = False
                        elif fuerza_maxima == int(datos[key]):
                            identidad_maxima += '  y ' + datos['identidad']
                            peso_mayor_fuerza += ' y ' + datos['peso']
            print(f'La identidad es {identidad_maxima} y su peso es {peso_mayor_fuerza}')
        case 'C' | 'c':
            '''Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)'''
            bandera_altura = True
            for datos in lista_personajes:
                for key in datos.keys():
                    if key == 'altura':
                        if bandera_altura == True or float(datos[key]) < altura_minima:
                            altura_minima = float(datos[key])
                            identidad_altura_minima = datos['identidad']
                            nombre_altura_minima = datos['nombre']
                            bandera_altura = False
                        elif altura_minima == float(datos[key]):
                            identidad_altura_minima += '  y ' + datos['identidad']
                            nombre_altura_minima += ' y ' + datos['nombre']     
            print(f'La identidad es {identidad_altura_minima} y su nombre es {nombre_altura_minima}')
        case 'D' | 'd':
            '''D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)'''
            acumulador_peso = 0
            contador = 0
            for datos in lista_personajes:
                for key in datos.keys():
                    if key == 'peso' and  datos['genero'] == 'M':
                        acumulador_peso = acumulador_peso + float(datos[key])
                        contador = contador + 1

            promedio = acumulador_peso / contador
            print(f'El promedio del peso de los supereheores masculinos es {promedio}')
        case 'E' | 'e':
            '''E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino'''
            acumulador_fuerza = 0
            contador = 0
            for datos in lista_personajes:
                for key in datos.keys():
                    if key == 'fuerza' and  datos['genero'] == 'F':
                        acumulador_fuerza = acumulador_fuerza + float(datos[key])
                        contador = contador + 1

            promedio_fuerza_femenina = acumulador_fuerza / contador

            print(f'El promedio de fuerza femenina es de : {promedio_fuerza_femenina}')

            for datos in lista_personajes:
                for key in datos.keys():
                    if key == 'fuerza' and float(datos[key]) > promedio_fuerza_femenina:
    
                        print(datos['nombre'])
                        print(datos['peso'])  
                        print(datos[key])
                        print('---------------------')        
        case'F' | 'f':
            continuar = False
        case _:
            print('No se reconoce')





