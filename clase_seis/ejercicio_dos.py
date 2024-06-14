'''
con el append agrego elementos al final de la lista 
array trabajado de manera secuencial: muestro los elementos como se fueron agregando
son arrays (vectores) unidimensional, tiene una unica dimension
'''

palabra = input("Ingresa una palabra: ")

for i in range(len(palabra)):
    print(palabra[i])

for letra in palabra:
    print(letra)