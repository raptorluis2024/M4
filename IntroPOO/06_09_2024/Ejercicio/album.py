import datetime 
from foto import Foto

class Album():
    def __init__(self, fecha: datetime = datetime.datetime.now(), nombre : str = "no-name") -> None:
        self.__fechacreacion = fecha
        self.__nombre = nombre
        self.__listafotos = []
    
    @property
    def fechacreacion(self):
        return self.__fechacreacion
    @fechacreacion.setter
    def fechacreacion(self, fecha):
        self.__fecha = fecha
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @property
    def fotos(self):
        return self.__listafotos
    
    def __str__(self) -> str:
        return f"Album {self.nombre}, Fecha Creacion: {self.fechacreacion.strftime("%m/%d/%Y, %H:%M:%S")}"
    
    def addFoto(self, foto:Foto):
        ## se agrega la foto a la lista de fotos
        self.__listafotos.append(foto)
        
    def listar_fotos(self):
        print("Listado de Fotos")
        for f in self.__listafotos:
            print(f)
            
              
        
        