def listar(lista1:list, lista2:list, lista3:list): #se debe pasar 3 listas
    '''
    enlista los elementos de dos listas basandose en el estado de la tercer lista
    '''
    for i in range(len(lista1)): #el len es el tamaño, si la lista tiene 5 elementos, len(lista) es = a 5 
        if lista1[i] != "LIBRE":
            mostrar(lista2, lista3, i)
 

def mostrar(lista:list, lista1:list, indice:int): #2 listas + indice
    '''

    '''
    print(f"{lista[indice]}, {lista1[indice]}")  

def buscar(lista:list,dato:str)-> int:
    """
    busca un dato en una lista.
    Si lo encuentra retorna el indice.
    Si no lo encuentra retorna -1
    """
    retorno = -1
    for i in range(len(lista)):
        if dato == lista[i]:
            retorno = i
            break
    return retorno

def validar_respuesta(rta:str)-> bool:
    retorno = False
    if rta == "S" or rta == "s" or rta=="N" or rta == "n":
        retorno = True
    return retorno

def alta(mensaje:str):
    dato = input(mensaje)
    return dato

def buscar_libre(lista:list,libre:str)->int:
    retorno=-1
    for i in range(len(lista)):
        if lista[i] == libre:
            retorno=i
            break
    return retorno

def lista_vacia(lista:list,libre:str)->bool:
    retorno=True
    for i in range(len(lista)):
        if lista[i]!=libre:
            retorno=False
            break
    return retorno

   
   