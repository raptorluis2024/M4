from error import DimensionError
class Foto():
    MAX = 5000

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        if ancho < 1 or ancho > Foto.MAX:
            raise DimensionError(f"Error en ancho foto {ruta}",ancho, Foto.MAX)
            return None
        elif alto < 1 or alto > Foto.MAX:
            raise DimensionError(f"Error en alto foto {ruta}",alto,Foto.MAX)
            return None
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            if ancho < 1 or ancho > Foto.MAX:
                raise DimensionError("Ancho", ancho, Foto.MAX)
            else:
                self.__ancho = ancho
        except DimensionError as de:
            print(de)
            

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            if alto < 1 or alto > Foto.MAX:
                raise DimensionError("Alto", alto, Foto.MAX)
            else:
                self.__alto = alto
        except DimensionError as de:
            print(de)
            
    def __str__(self) -> str:
        return f"Alto: {self.alto} Ancho: {self.ancho} Ruta: {self.ruta} "
    
