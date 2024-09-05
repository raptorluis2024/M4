class DimensionError(Exception):
    def __init__(self, mensaje:str, dimension:int=None, maximo:int=None ) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            return f"{self.mensaje} {self.dimension} Excede al máximo que es {self.maximo}"
    
        

