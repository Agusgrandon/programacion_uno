'''
operadores ternarios, funciones lamba
'''
x = 43
resultado = "Es la respuesta" if x == 42 else "anduviste cerca"
print(resultado)

#FUNCIONES LAMBDA

def suma(numero1:int, numero2:int):
    return numero1 + numero2

resultado_dos = suma(2,2)
print(resultado_dos)

suma_dos = lambda a,b : a + b
print(suma_dos(3,3))

#ARCHIVOS

#Para abrir un archivo con Python, podemos usar la función open. archivo = open(nombre_archivo, modo)
archivo = open('texto.txt', 'r')

#Para cerrar un archivo con Python, podemos usar la función close.
archivo.close()


