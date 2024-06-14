# A. Normalizar datos (No se debe poder acceder a los otros puntos)
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de genero NB
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de genero NB 
# H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# J. Listar todos los superhéroes agrupados por color de ojos.
# K. Listar todos los superhéroes agrupados por tipo de inteligencia

from os import system
from listado import lista_personajes
from funciones_dos import *


continuar = True


while continuar:

    print('\t A- Normalizar datos (No se debe poder acceder a los otros puntos) \n \tB- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB \n \tC- Recorrer la lista y determinar cuál es el superhéroe más alto de género F \n \tD- Recorrer la lista y determinar cuál es el superhéroe más alto de género M \n \tE- Recorrer la lista y determinar cuál es el superhéroe más débil de género M \n \t F- Recorrer la lista y determinar cuál es el superhéroe más débil de género NB \n \t G- Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB \n \t H- Determinar cuántos superhéroes tienen cada tipo de color de ojos. \n \t I- Determinar cuántos superhéroes tienen cada tipo de color de pelo. \n \t J- Listar todos los superhéroes agrupados por color de ojos. \n \t K-Listar todos los superhéroes agrupados por tipo de inteligencia) \n \t L- Salir')
    opcion = input('Ingrese opcion:')

    system('cls')

    match(opcion):
        case 'A' | 'a':
            stark_normalizar_datos(lista_personajes)
            print(lista_personajes)
        case 'B' | 'b':
            # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de genero NB
            for personaje in lista_personajes:
                if personaje['genero'] == "NB":
                    print( personaje['nombre'])
                    print('--------------------------')
        case 'C' | 'c':
            # C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            resultado = clave_max_min_genero(lista_personajes, "altura", "F", "MAX")
            print (resultado)
        case 'D' | 'd':
            # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            resultado = clave_max_min_genero(lista_personajes, "altura", "M", "MAX")
            print (resultado)
        case 'E' | 'e':
            # E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
            resultado = clave_max_min_genero(lista_personajes, "fuerza", "M", "MIN")
            print (resultado)
        case 'F' | 'f':
            # F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
            resultado = clave_max_min_genero(lista_personajes, "fuerza", "NB", "MIN")
            print (resultado)
        case 'G' | 'g':
            # G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de genero NB
            resultado = promedio_por_genero(lista_personajes, "fuerza", "NB")
            print (resultado)
        case 'H' | 'h':
            # H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            contar_por_caracteristica(lista_personajes, "color_ojos")
        case 'I' | 'i':
            # I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            contar_por_caracteristica(lista_personajes, "color_pelo")
        case 'J' | 'j':
            # J. Listar todos los superhéroes agrupados por color de ojos.
            listar_por_caracteristica(lista_personajes, "color_ojos")
        case 'K' | 'k':
            # K. Listar todos los superhéroes agrupados por tipo de inteligencia
            listar_por_caracteristica(lista_personajes, "inteligencia")
        case 'L' | 'l':
            continuar = False
