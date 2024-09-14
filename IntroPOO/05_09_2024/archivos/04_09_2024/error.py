class Error(Exception):
    pass

class EdadError(Error):
    def __init__(self, mensaje, edad) -> None:
        self.edad = edad
        self.mensaje=mensaje
        
try:
    edad = int(input("ingrese una edad"))
    if edad < 18:
        raise EdadError("Error en la edad", edad)
except EdadError as e:
    print(f"{e.mensaje} {e.edad}")
except ValueError as ve:
    print(ve)
    