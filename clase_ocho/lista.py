#Lista paralela
'''
nombres = ["Pedro", "Ana", "Jose"]
edades = [23, 30, 18]
estados = ["OCUPADO", "OCUPADO", "OCUPADO"]

def mostrar_lista(lista_estado:list, lista_uno:list, lista_dos:list):
    for i in range(len(lista_estado)):
        if lista_estado[i] == "OCUPADO":
            print(f"{lista_uno[i]} {lista_dos[i]}")

mostrar_lista(estados, nombres, edades)

for i in range(len(personas)):
    print(personas[i][0], personas[i][1]) 
     #tomo la posicion 0 y muestro el primer dato, despues vuelve al for y ya vale 1, entonces sigue al siguiente dato
'''
#listas anidadas 
from index import *

personas = [["OCUPADO","Pedro", 23, "M"], ["LIBRE", "Ana", 30, "F"], ["OCUPADO", "Jose", 18, "M"]]


listar_lista_de_listas(personas)
 





