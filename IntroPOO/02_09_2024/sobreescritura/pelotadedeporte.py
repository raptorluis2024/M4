#Sobreescritura haciendo llamado a método de clase padre
class PelotaDeDeporte():
    def __init__(self, color: str):
        self.__color = color

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color

class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color: str, cantidad_hexagonos: int):
        super().__init__(color) # se ejecuta constructor de PelotaDeDeporte
        self.__cantidad_hexagonos = cantidad_hexagonos

    @property
    def cantidad_hexagonos(self):
        return self.__cantidad_hexagonos
    
    @property
    def color(self):
        return f"{self.color} al estilo Pelota de Futbol"
    
"""
la pelota de futbol sabe obtener el color como su padre, pero al sobreescribirlo lo hace a su manera
""" 
    



pdf = PelotaDeFutbol("Blanco y Negro", 15)
# Salida: Blanco y Negro
print(pdf.color)
# Salida: 15
print(pdf.cantidad_hexagonos)