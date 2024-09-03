from foto import Foto

class FotoPerfil(Foto):
    def __init__(self) -> None:
        super().__init__("extras/user.png", 400, 400 )
        self.__recorte = [(0,0),(self.ancho, 0),(0, self.alto),(self.ancho, self.alto)]