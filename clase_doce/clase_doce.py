'''
diccionarios, el dato es inmutable, no hay dos datos iguales, el diccionario es clave-valor
se pone con key y un valor, el valor puede ser cualquier cosa, se coloca con {}
cuando hago el for SOLO devuelve la clave, NO el valor, despues hago diccionadrio print(clave,diccionario[clave])
las tuplas son inmutables, son diferentes a las listas, van con (), la lista [] si son mutables, se pueden cambiar
el deepcopy es para copiar diccionarios dentro de diccionarios, si solo quiere copiar un valor uso .copy
el get permite consultar el valor de una key
el keys consulta la clave
items devulve la key y su valor, contenido en una lista 
pop busca y elimina la key que queres
update agrega un elemento al diccionario o lo pisa si ya existe
clear elimina todo el contenido del diccionario
set, conjunto de datos, en estos los elementos no se repiten 
'''

from copy import deepcopy

#persona = {'nombre': 'Leo', 'apellido': 'messi', 'edad': 37}



'''persona_copia = persona

print(persona)
print(persona_copia)

persona['nombre'] = 'mateo'

print(persona)
print(persona_copia)

persona_copia['apellido'] = 'martinez'

print(persona)
print(persona_copia)'''

diccionario = {
    'name' : ['Marty','Mcfly'], 
    'edad' : 18, 
    'apellido': 'alguno', 
    'color': 'rojo', 
    'direccion': {'numero': 1234},
    'posicion': (1,0)
}
'''diccionario_copia = diccionario.copy()

diccionario['name'][0] = 'Messi'
diccionario['color'] = 'azul'
diccionario['edad'] = 50
diccionario['apellido'] = 34
diccionario['direccion']['numero'] = 9999

print(diccionario)
print(diccionario_copia)'''

'''dic_copia = deepcopy(diccionario)

diccionario['name'][0] = 'Messi'
diccionario['color'] = 'azul'
diccionario['edad'] = 50
diccionario['apellido'] = 34
diccionario['direccion']['numero'] = 9999

print(diccionario)
print(dic_copia)


dic_copia['name'][0] = 'Juan'
dic_copia['color'] = 'verde'
dic_copia['edad'] = 37
dic_copia['apellido'] = 'none'
dic_copia['direccion']['numero'] = 'uno'

print(diccionario)
print(dic_copia)'''

'''print( diccionario.get('name', 'ERROR!!'))
print( diccionario.get('hola', True))
'''
dic_keys = list(diccionario.keys())
dic_values = list(diccionario.values())
dic_items = list(diccionario.items())

'''for key_value in dic_items:
    print(key_value[0], key_value[1])

dic_keys.sort()
dic_keys.append('hola')
dic_values.append('hola')'''

#print(dic_items)

'''def agregar():
    print('Error!!')
    return False

print(diccionario.pop('posiciondd', agregar()))
print(diccionario)'''

'''
diccionario.update({'mascota': 'gato'})
diccionario.update({'apellido': 'Rojo'})

print(diccionario)

diccionario.clear()

print(diccionario)'''



'''def en_caso_no_key(mensaje):
    print(mensaje)
    return False

print(diccionario.pop('posiciondd', 'error'))
print(diccionario.pop('posicion', 'error'))
print(diccionario)'''



apellido = diccionario.get('apellidos', 'not key `apellidos`')

print(apellido)

persona = {'id': 0, 'name': 'Leo', 'age': 37, 'addr': {'street': ' calle falsa 123 ', 'city': 'Miami'}, 'mascota': {'nombre': 'Hulk'}}
persona_2 = {'id': 1, 'name': 'Mateo', 'age': 7, 'addr': {'street': ' calle falsa 123', 'city': 'CABA'}, 'mascota': {'nombre': 'Mia'}}

personas = [persona, persona_2]

for pers in personas:
    for key_value in pers.items():
        #print(key_value)
        if(type(key_value[1]) == type(dict())):
            for key_value_2 in key_value[1].items():
                print(key_value_2[0], key_value_2[1])
        else:
            print(key_value[0], key_value[1])
        
    print('-------------------')
