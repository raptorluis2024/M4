class Error(Exception):
    pass

class LargoExcedidoException(Error):
    pass

class SubTipoInvalidoError(Error):
    def __init__(self, mensaje:str) -> None:
        super().__init__(mensaje)
