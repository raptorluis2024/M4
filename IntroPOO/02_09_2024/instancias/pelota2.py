"""
isinstance
Definición de la clase padre Al crear una instancia de una clase 
heredada se puede acceder a un método creado en su clase padre, la instancia (self)
evaluada mediante isinstance puede ser tanto de la clase padre, como de cualquier
clase hija que no haya sobrescrito el método donde se hace la evaluación.
Esto permite condicionar, entre otros,valores que se pueden asignar a atributos de la instancia.
"""
class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        if isinstance(self, PelotaDeTenis):
            self.__color = "Amarillo"
        else:
            self.__color = color
    @property
    def color(self) -> str:
        return self.__color
    
class PelotaDeTenis(PelotaDeDeporte):
    pass


p = PelotaDeTenis("Rojo")
# Salida: Amarillo
print(p.color)