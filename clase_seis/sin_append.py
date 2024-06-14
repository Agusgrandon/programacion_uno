'''
carga secuencial sin append
'''
nombres = ["A", "A", "A", "A", "A"]

for i in range(len(nombres)):
    nombre = input("Ingresa el nombre: ")
    nombres[i] = nombre

for i in range(len(nombres)):
    print(nombres[i])

'''
carga aleatoria
'''
nombres = ["A", "A", "A", "A", "A"]

for i in range(len(nombres)):
    nombre = input("Ingresa el nombre: ")
    indice = input("Ingrese el indice: ")
    indice = int(indice)
    while indice < 0 or indice > len(nombres) or nombres[indice] != "A":
           indice = input("Error, reingrese el indice: ")
           indice = int(indice)
       
    nombres[indice] = nombre

for i in range(len(nombres)):
    print(nombres[i])


