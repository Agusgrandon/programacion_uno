from animales import Mascota
from dni import Dni
class Gato (Mascota):
    def __init__(self, raza, peso, nombre, color, maullido, dni):
        super().__init__(raza, peso, nombre, color)
        self.__maullido = maullido
        self.__dni = Dni(dni)
        
    @property
    def dni(self):
        return self.__dni
    def mover(self):
        super().comer()
        print(f'El gato {self.nombre} se mueve')
        super().mover()
        
        
    def comer(self):
        print('El gato come')