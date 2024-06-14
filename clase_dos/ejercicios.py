from matematica.funcionesdos import *

# o tambien: from funciones import sumar, resta etc, si pongo * importo todo

#2. Crear una función que verifique si un número dado por argumento es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_par(numero):
    if(numero % 2 == 0):
        print(f"el numero {numero} es par")
    else:
        print(f"el numero {numero} es impar")

verificar_par(2)

#si no:

def es_par(numero:int) -> bool:
    '''
    verifica si el numero ingresado es par o no
    numero: -> int
    return: -> bool
    '''
    return (numero % 2 == 0)

par = es_par(4)
print(par)

#tambien se puede asi:
def verificar_otra_vez_par (numero:int) -> bool:
    retorno = False
    if numero != 0:

        if numero < 0:
            numero *= -1

        while numero > 1:
            numero -= 2
        
        if numero == 0:
            retorno = True
        
    return retorno

verificacion = verificar_otra_vez_par(0)

print(verificacion)


'''
3. Define una función que encuentre el máximo de tres números. 
   La función debe aceptar tres argumentos y devolver el número más grande.
'''

def encontrar_maximo(numero_uno, numero_dos, numero_tres):
        '''
        encuentra el numero mas grande
        '''
        if numero_uno > numero_dos and numero_uno < numero_tres:
             numero_maximo = numero_uno
        elif numero_dos > numero_tres:
             numero_maximo = numero_dos
        else:
             numero_maximo = numero_tres

        return numero_maximo

mayor_numero = encontrar_maximo(4,6,1)
print(mayor_numero)

#si no tambien se puede
def numero_maximo (numero_a:int, numero_b:int, numero_c:int)->int:
    """
    Devuelve el numero maximo 
    
    Args:
    numero_a (int): Se debe ingresar un numero entero 
    numero_b(int): Se debe ingresar un numero entero
    numero_c(int): Se debe ingresar un numero entero

    Returns:
    tipo_de_retorno (int): Devuelve el valor maximo de los tres parametros ingresados
    """
    retorno = None

    if numero_a == numero_b and numero_a == numero_c:
        retorno = numero_a
    else:
        if numero_a > numero_b and numero_a > numero_c:
            retorno = numero_a

        elif numero_b > numero_c:
            retorno = numero_b

        else:
            retorno = numero_c

    return retorno

print(numero_maximo(3,2,1))

'''
4. Diseña una función que calcule la potencia de un número. 
   La función debe recibir la base y el exponente como argumentos y devolver el resulta
'''

def calcular_potencia(numero_base, potencia):
     '''
     calcula la potencia de un numero
     '''
     calculo = numero_base * numero_base * numero_base
     return calculo

potencia_de_un_numero = calcular_potencia(3, 2)
print(potencia_de_un_numero)

#4. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

#base=4
#exponente=3
def potencia(base:int, exponente:int)->int:
    '''
    Summary: 
    Recibe dos argumentos, base y exponente, calcula al potencia y devuelve el resulatdo
    Args: 
    base (int): base 
    exponente (int): exponente
    
    Returns:
    int: resultado de la base elevado a la potencia
    """

    '''
    if exponente==0:
        resultado=1
    else:
        resultado=1
    
        for e in range(exponente):
            resultado*=base
    return resultado

print(potencia(2,16))

print(funcion_sumar(2,2))

'''
factorizar

'''

def calcular_factorial (natural:int) -> int:
    """
    Summary:
    Esta funcion toma un numero natural y realiza la operacion factorial.
    
    Args:
    natural (int): Numero natural mayor o igual 0.
    
    Returns:
    int: Devuelve resultado. En caso de un argumento negativo retornara como error "-999".
    """
    resultado = 1

    if natural >= 0:
        for numero in range(natural, 0, -1):
            resultado *= numero
    else:
        resultado = -999
    return resultado

print(calcular_factorial(2))
