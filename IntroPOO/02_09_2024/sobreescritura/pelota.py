##SOBREECRITURA
class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        self.__color = color

    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, color) -> None:
        self.__color = color

class PelotaDeTenis(PelotaDeDeporte):
    def __init__(self) -> None:
        self.__color = "Amarillo"

    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, color: str) -> None:
        self.__color = color
    
pdt = PelotaDeTenis()
pdt.color = "Rojo"
# Salida: Amarillo
print(pdt.color)