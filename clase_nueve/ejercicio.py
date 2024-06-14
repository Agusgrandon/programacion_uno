'''
ordenar dos listas paralelas con sexo y nombre, ambas en ascendentes
VECTORES
'''
generos = ["F", "F", "M", "F", "M", "M", "M", "F"]
nombres = ["Maia","Sebastiana", "Alan", "Daniela", "Pedro", "Leandro", "Alan", "Luisa"]
edades = [20, 19, 21, 25, 23, 24, 26, 22]
apellidos = ["Garcia", "Lopez", "Lima", "Garcia", "Martino", "Lopez", "Martino", "Grandon"]

#ordenamos por dos criterios: el de generos, primero F y despues M
# recorremos las listas
for i in range(len(generos)-1):
    auxiliar = None
    for j in range(i + 1,len(generos)):
        if (generos[i] > generos[j]) or (generos[i] == generos[j] and apellidos[i] > apellidos[j]) or (generos[i] == generos[j] and apellidos[i] == apellidos[j] and nombres[i] > nombres[j]):
            auxiliar = generos[j]
            generos[j] = generos[i]
            generos[i] = auxiliar
            # lo tengo que hacer por cada lista que tenga 
            auxiliar = nombres[j]
            nombres[j] = nombres[i]
            nombres[i] = auxiliar

            auxiliar = edades[j]
            edades[j] = edades[i]
            edades[i] = auxiliar

            auxiliar = apellidos[j]
            apellidos[j] = apellidos[i]
            apellidos[i] = auxiliar

# este for concatena y muestra TODOS los items, si no lo hago solo muestra uno
for i in range(len(generos)):
    print(generos[i] + " " + apellidos[i] + " " + nombres[i] + " " + str(edades[i]))

'''        elif generos[i] == generos[j] and nombre[i] > nombre[j]:
            auxiliar = generos[j]
            generos[j] = generos[i]
            generos[i] = auxiliar

            auxiliar = nombre[j]
            nombre[j] = nombre[i]
            nombre[i] = auxiliar

            auxiliar = edades[j]
            edades[j] = edades[i]
            edades[i] = auxiliar
            
            si no uso el or en el primer if, tambien se puede con el elif'''





