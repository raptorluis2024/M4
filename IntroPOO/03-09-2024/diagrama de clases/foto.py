class Foto():
    def __init__(self, imagen: str, ancho: int, alto: int) -> None:
        self.__imagen = imagen
        self.__ancho = ancho
        self.__alto = alto
        self.__reacciones = 0

    @property
    def imagen(self) -> str:
        return self.__imagen
    @imagen.setter
    def imagen(self, imagen: str) -> None:
        self.__imagen = imagen
    @property
    def ancho(self) -> int:
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho: int) -> None:
        self.__ancho = ancho
    @property
    def alto(self) -> int:
        return self.__alto
    @alto.setter
    def alto(self, alto: int) -> None:
        self.__alto = alto
    @property
    def reacciones(self) -> int:
        return self.__reacciones
    @reacciones.setter
    def reacciones(self, reacciones: int) -> None:
        self.__reacciones = reacciones
