'''
arrays multidimensionales
'''
#ES UNIDIMENSIONAL, EMPIEZA EN LA A Y TERMINA EN LA S, se lo conoce como vector
nombre = "agus"
#matriz: tiene varios elementos, i hace referencia a las 8 filas, y j hace referencia a las columnas(una por cada letra)
nombres = ["Maia","Sebastiana", "Alan", "Daniela", "Pedro", "Leandro", "Alan", "Luisa"]
#aca tengo dos dimensiones, es bidimensional
numeros = [[20, 19, 21, 25],[23, 24, 26, 22]]

'''for i in nombre:
    print(i)

for letra in range (len(nombre)):
    print(nombre[letra])'''

#este for recorre la lista, y el segundo recorre cada indice de los string
for i in range (len(nombres)):
    for j in range (len(nombres[i])):
        print(nombres[i][j])
        
bandera = False
for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        if bandera == False or numeros[i][j] > numero_max:
            numero_max = numeros[i][j]
        if bandera == False or numeros[i][j] < numero_min:
            numero_min = numeros[i][j]
            bandera = True     
print(numero_max, numero_min)

#ORDENAR LA FILA DE LA MATRIZ
'''
matriz = [[2, 1, 3, 7],[5, 8, 6, 4]]
    for i in range(len(matriz)):
        for j in range(len(matriz[i]) - 1):
            for k in range(j + 1, len(matriz[i])):
                if matriz[i][j] > matriz[i][k]:
                    auxiliar = matriz[i][j]
                    matriz[i][j] = matriz[i][k]
                    matriz[i][k] = auxiliar
print(matriz)
'''
#ordenar todo 
matriz = [[2, 1, 3, 7],[5, 8, 6, 4]]

for i in range(len(matriz)):
    for j in range(len(matriz[i]) - 1):
        for k in range(j + 1, len(matriz[i])):
            if matriz[i][j] > matriz[i][k]:
                auxiliar = matriz[i][j]
                matriz[i][j] = matriz[i][k]
                matriz[i][k] = auxiliar

print(matriz)



      