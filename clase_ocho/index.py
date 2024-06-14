def listar_lista_de_listas(lista:list):
    #recorro la lista
    for i in range(len(lista)):
        #seteo/inicializacion de variables
        bandera_mensaje = True
        bandera_ocupado = True
        estado_ocupado = False
        
        #recorro cada elemento (es una lista) de la lista 
        for j in range(len(lista[i])):
            #controlo el primer elemento que es OCUPADO/LIBRE para no imprimirlo
            if bandera_ocupado == True: 
                bandera_ocupado = False
                #controlo que el elemento este ocupado para mostrarlo a partir de la segunda repeticion de j
                if lista[i][j] == "OCUPADO":
                    estado_ocupado = True
            #controlo que el estado este ocupado en cada elemento (es una lista) de la lista general
            elif estado_ocupado == True:
                #si no es un dato no es str lo paso/casteo a str
                if type(lista[i][j]) == int:
                    lista[i][j] = str(lista[i][j])
                #quito el espacio en blanco del primer mensaje
                if bandera_mensaje == True:
                    mensaje = lista[i][j]
                    bandera_mensaje = False
                #concateno los datos con un espacio en blanco en medio de ellos
                else:
                    mensaje += " " + lista[i][j]
        #imprimo solamente si esta ocupado
        if estado_ocupado == True:
            print (mensaje)




