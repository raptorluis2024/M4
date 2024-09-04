from utiles.madera import Pino

class Casa():
    def __init__(self) -> None:
        self.__pisos = 1
        self.__madera = Pino("baja",100)
        
    @property
    def madera(self):
        return self.__madera
        
c = Casa()
print(c.madera.densidad,c.madera._duracion)
print(c.madera._calidad)
print(c.madera)
    

