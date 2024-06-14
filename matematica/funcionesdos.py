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