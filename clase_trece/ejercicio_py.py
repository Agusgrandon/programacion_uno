'''
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia
NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú'''

from os import system
from lista import lista_personajes
from funciones import *

continuar = True


while continuar:

    print('\t A- Nombres de superheroes NB \n \tB- Superheroe Femenino más alto \n \tC- Superheroe masculino más alto \n \tD- Superheroe masculino mas debil \n \tE- Superheroe No binario mas debil \n \t F- Promedio fuerza NB \n \t G- Color de ojos \n \t H- Color de pelo \n \t I- Lista superheroes por color de ojos \n \t J- Listar por tipo de inteligencia \n \t K- Salir')
    opcion = input('Ingrese opcion:')

    system('cls')

    match opcion:
        case 'A' | 'a':
            #A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
            system('cls')
            for personaje in lista_personajes:
                if personaje['genero'] == "NB":
                    print( personaje['nombre'])
                    print('--------------------------')
            
        case 'B'  | 'b':
            #B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            resultado = clave_max_min_genero(lista_personajes, "altura", "F", "MAX")
            print (resultado)

        case 'C' | 'c':
            #C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            resultado = clave_max_min_genero(lista_personajes, "altura", "M", "MAX")
            print (resultado)

        case 'D' | 'd':
            #D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
            resultado = clave_max_min_genero(lista_personajes, "fuerza", "M", "MIN")
            print (resultado)

        case 'E' | 'e':
            #E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
            resultado = clave_max_min_genero(lista_personajes, "fuerza", "NB", "MIN")
            print (resultado)

        case "F" | "f":
            #F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
            resultado = promedio_por_genero(lista_personajes, "fuerza", "NB")
            print (resultado)

        case "G" | "g":
            #G. Determinar cuántos superhéroes tienen cada tipo de color de ojos
            contar_por_caracteristica(lista_personajes, "color_ojos")
            # lista_color_ojos = []
            # print("Color\t\t\t\tCantidad")
            # print("----------------------------------------")
            # for personaje in lista_personajes:
            #     lista_color_ojos.append(personaje["color_ojos"].capitalize())
            # set_color_ojos = set(lista_color_ojos)
            # for color in set_color_ojos:
            #     contador = 0 
            #     for personaje in lista_personajes:
            #         if color == personaje["color_ojos"].capitalize():
            #             contador += 1 
            #     if len(color) < 10:
            #         print(f"{color}\t\t\t\t{contador}")
            #     else:
            #         print(f"{color}\t\t{contador}")
            # conteo_colores_ojos = {}
            # for personaje in lista_personajes:
            #     color = personaje["color_ojos"]
            #     if color in conteo_colores_ojos:
            #         conteo_colores_ojos[color] += 1
            #     else:
            #         conteo_colores_ojos[color] = 1


            # for color, conteo in conteo_colores_ojos.items():
            #     print(f"{color}: {conteo}")

        case "H" | "h":
            #H. Determinar cuántos superhéroes tienen cada tipo de color de pelo
            contar_por_caracteristica(lista_personajes, "color_pelo")
            # lista_color_pelo = []
            # print("Color\t\tCantidad")
            # print("-----------------------------")
            # for personaje in lista_personajes:
            #     if personaje["color_pelo"] != "":
            #         lista_color_pelo.append(personaje["color_pelo"].capitalize
            # ())
            # set_color_pelo = set(lista_color_pelo)
            # for color in set_color_pelo:
            #     contador = 0 
            #     for personaje in lista_personajes:
            #         if color == personaje["color_pelo"].capitalize():
            #             contador += 1 
            #     if len(color) < 10:
            #         print(f"{color}\t\t{contador}")
            #     else:
            #         print(f"{color}\t{contador}")
        case "I" | "i":
            #I. Listar todos los superhéroes agrupados por color de ojos.
            listar_por_caracteristica(lista_personajes, "color_ojos")
        
        case "J" | "j":
            #J. Listar todos los superhéroes agrupados por tipo de inteligencia
            listar_por_caracteristica(lista_personajes, "inteligencia")
        
            # diccionario_inteligencia = {}

            # for personaje in lista_personajes:
            #     inteligencia = personaje["inteligencia"].capitalize()
            #     if inteligencia != "":
            #         if inteligencia in diccionario_inteligencia:
            #             diccionario_inteligencia[inteligencia] += " - " + personaje["nombre"]
            #         else:
            #             diccionario_inteligencia[inteligencia] = personaje["nombre"]


            # for inteligencia, nombres in diccionario_inteligencia.items():
            #     print(f"{inteligencia}: {nombres}")
            #     print("------------")
            
        case'K' | 'k':
            continuar = False
            
        case _:
            print('No se reconoce')
    pausa()


