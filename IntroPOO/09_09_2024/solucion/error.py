class Error(Exception):
    pass

class LargoExcedidoException(Error):
    def __init__(self, mensaje:str) -> None:
        self.__mensaje = mensaje
            
    @property
    def mensaje(self):
        return self.__mensaje

class SubTipoInvalidoError(Error):
    def __init__(self, mensaje:str) -> None:
        self.__mensaje = mensaje
            
    @property
    def mensaje(self):
        return self.__mensaje
    

