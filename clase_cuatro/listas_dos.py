'''
leng es la cantidad de indices que tiene la lista
'''
import random
datosPersonales = ['leo', "messi", 37, "argentino"]

def mostrarDatos(datos:list):
    """_summary_

    Args:
        datos (list): _description_
    """
    for i in range(len(datos)):
        print(datos[i])

datosPersonales.append('miami')

#mostrarDatos(datosPersonales)

numeros = []

for numero in range(10):
    numeroRandom = random.randint(1, 1000)
    numeros.append(numeroRandom)
    
#mostrarDatos(numeros)


def buscarDato(lista, indice):
    retorno = False    
    if indice >= 0 and indice < len(lista):
        retorno = lista[indice]
    return retorno
        
#buscarDato(numeros, 0)
#buscarDato(numeros, 9)

#mostrarDatos(datosPersonales)
#datosPersonales.remove(37)
#mostrarDatos(datosPersonales)

itemBorrado = datosPersonales.pop()
#mostrarDatos(datosPersonales)
#print(f" fue borrado {itemBorrado}")


numerosAux = []

contador = 0

'''
for i in range(len(numeros2)):
    if numeros2[i - contador] == 5:
        numeros2.pop(i - contador)
        contador += 1

'''

"""for numero in numeros2:
    if numero != 5:
        numerosAux.append(numero)"""

#mostrarDatos(numerosAux)

numerosMinimo = None

numeros2 = [0, 2, 50, 23, 8, 9]

for i in range(len(numeros2)):
    for j in range(len(numeros2)-i):
        if i > 0 and numeros2[j] > numeros2[j+1]:
            aux = numeros2[j + 1]
            numeros2[j + 1] = numeros2[j]
            numeros2[j] = aux
        
mostrarDatos(numeros2)
'''
este código es una implementación del algoritmo de ordenamiento burbuja en Python. Básicamente, este algoritmo compara repetidamente pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Aquí está la explicación línea por línea:

for i in range(len(numeros2)):: Este bucle externo itera sobre cada elemento en numeros2. len(numeros2) devuelve la longitud de la lista numeros2, y range(len(numeros2)) genera una secuencia de números desde 0 hasta la longitud de numeros2 menos 1. i tomará los valores de esta secuencia en cada iteración.

for j in range(len(numeros2)-i):: Este bucle interno itera sobre cada elemento en numeros2 hasta len(numeros2) - i - 1. Esto es porque después de cada pasada exterior del bucle, el elemento más grande ya está en su posición final, por lo que no es necesario compararlo nuevamente.

if i > 0 and numeros2[j] > numeros2[j+1]:: Esta condición verifica si i es mayor que 0 (es decir, si no estamos en la primera pasada del bucle externo) y si el elemento actual es mayor que el siguiente elemento en la lista. Si ambas condiciones son verdaderas, significa que los elementos están en el orden incorrecto y necesitan ser intercambiados.

aux = numeros2[j + 1]: Se guarda temporalmente el valor del siguiente elemento en la variable aux.

numeros2[j + 1] = numeros2[j] y numeros2[j] = aux: Aquí se intercambian los elementos. El valor del elemento actual (numeros2[j]) se reemplaza con el valor del siguiente elemento (numeros2[j + 1]) y viceversa.

mostrarDatos(numeros2): Finalmente, después de que se haya completado el proceso de ordenamiento, se llama a una función mostrarDatos pasando la lista ordenada numeros2 como argumento. Presumiblemente, esta función mostrará los datos ordenados de alguna manera.

En resumen, este código ordena la lista numeros2 utilizando el algoritmo de ordenamiento burbuja y luego muestra los datos ordenados.
'''



