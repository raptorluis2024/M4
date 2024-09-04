class Madera():
    def __init__(self, densidad:str, duracion:int) -> None:
        self.__densidad = densidad
        self._duracion = duracion
    @property
    def densidad(self): 
        return self.__densidad
    @densidad.setter
    def densidad(self, densidad:str):
        self.__densidad = densidad
    
class Pino(Madera):
    def __init__(self, densidad: str, duracion: int) -> None:
        super().__init__(densidad, duracion)
        self._calidad = "baja"
        
    def __str__(self):
        return f"densidad {self.densidad} duracion {self._duracion}"

if __name__ == "__main__":
    p = Pino("sss",1000)
    print(p)