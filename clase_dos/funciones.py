def funcion_sumar(numero_uno, numero_dos):
   return numero_uno + numero_dos
#es posicional, lo puedo poner en distintos lugares y se sigue tomando el valor que guarde en el nombre
suma = funcion_sumar(33,1)
print("La suma es", suma)

def funcion_restar(numero_uno, numero_dos):
   return numero_uno - numero_dos

resta = funcion_restar(33,1)
print("La suma es", resta)

def funcion_multiplicar(numero_uno, numero_dos):
   return numero_uno * numero_dos

multiplicacion = funcion_multiplicar(33,1)
print("La suma es", multiplicacion)

def funcion_dividir(numero_uno, numero_dos):
   resultado = 0
   if numero_dos != 0:
      resultado = numero_uno / numero_dos
      
   return resultado

print(funcion_dividir(numero_uno=6, numero_dos=9))

'''
todas las variables tienen un espacio en la memoria, en una direccion de la memoria, 
la variable esta guardada en una direccion de memoria, CUANDO HAGO EL PASO POR REFERENCIA
el cambio que hago en la funcion afecta a la variable porque comparten la misma direccion de memoria
por valor es una copia, por referencia se modifica
por referencia lo que trabajo en la funcion afecta la variable, por valor trabajo la variable en la funcion pero no afecta a la variable en si
no se puede poner mas de dos return
type me dice que tipo es el dato ingresado
en la firma hay que poner que dato devuelve 
'''