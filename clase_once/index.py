'''
cadenas de caracteres, poo
programacion orientada a objetos
diccionario: tiene clave (es unico)-valor (no se puede repertir)
'''
lista = []
diccionario_personajes = {
    'nombre' : 'Agus',
    'apellido' : 'Grandon',
    'edad' : ['20', '30', '10'],
    'genero' : 'F'
}
print(diccionario_personajes['nombre']) #asi accedo a la clave
#para modificarlo
diccionario_personajes['nombre'] = 'Hola'
print(diccionario_personajes['nombre'])
#para cambiarlo:
diccionario_personajes.update({'apellido': 'Messi'})
'''diccionario_personajes.pop('apellido') #remueve 
print(diccionario_personajes)'''

for caracteristica in diccionario_personajes.items():
    print(caracteristica)

#CLASS la primera letra siempre en mayuscula, no es lo mismo que un objeto, el sefl es todo lo que asignas, pertenece a esa clase
class Personajes:
    def __init__(self, id, nombre, edad, apellido) -> None:
        self.id = id
        self._nombre = nombre #atributo protegido _
        self.__edad = edad #y con dos guiones bajos es privado
        self.apellido = apellido
    #accion:
    def descripcion(self):
        return '{0}-{1}'.format(self._nombre, self.apellido)

personajeUno = Personajes(0, 'agus', 25, 'grandon')
personajeDos = Personajes(1, 'lionel', 34, 'messi')

print(personajeUno.descripcion())

