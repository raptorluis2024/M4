from datetime import date
from error import LargoExcedidoException
from anuncio import Video, Display, Social
class Campania():

    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date,anuncios:list ) -> None:
        
        self.__nombre = nombre
        self.__fechainicio = fecha_inicio
        self.__fechatermino = fecha_termino
        self.__anuncios = self.__agregarAnuncio(anuncios)

    def __agregarAnuncio(self,anuncios:list):
        anunciostemp =[]
        for a in anuncios:
            if a["tipo"] == "Video":
                anuncio = Video(a["url_archivo"],a["url_click"],a["sub_tipo"],a["duracion"])
            elif a["tipo"] == "Social":
                anuncio = Social(a["ancho"],a["alto"],a["url_archivo"],a["url_click"],a["sub_tipo"])
            elif a["tipo"] == "Display":
                anuncio = Display(a["ancho"],a["alto"],a["url_archivo"],a["url_click"],a["sub_tipo"])
            anunciostemp.append(anuncio)
        return anunciostemp
    
    def getAnuncio(self, pos:int):
        return self.__anuncios[pos]
    
    def contarAnuncios(self):
        v=d=s=0
        for a in self.__anuncios:
            if isinstance(a,Video):
                v += 1
            elif isinstance(a,Display):
                d += 1
            else:
                s += 1
        return v,d,s        

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre:str):
        if len(nombre) > 25:
            raise LargoExcedidoException("ERROR: Nombre de la campaña exede a 250 caracteres\n")    
        else:
            self.__nombre = nombre
    @property
    def fechainicio(self):
        return self.__fechainicio
    @fechainicio.setter
    def fechainicio(self, fechainicio: date):
        self.__fechainicio = fechainicio
    @property
    def fechatermino(self):
        return self.__fechatermino
    @fechatermino.setter
    def fechatermino(self, fechatermino: date):
        self.__fechatermino = fechatermino

    def __str__(self) -> str:
        v,d,s = self.contarAnuncios()
        return f"""Nombre de la campaña {self.__nombre}
                Anuncios: {v} Video, {d} Display, {s} Social """
    
    @property
    def list_anuncios(self):
        return self.__anuncios


    
if __name__ == "__main__":
    anuncios = [{"tipo":"Video","url_archivo":"http://www.campania2024.cl/archivo1.html", 
                 "url_click":"http://www.campania2024.cl","sub_tipo":"instream","duracion":100}]
    
    c = Campania("Campaña 1", date(2024,9,10),date(2024,9,17),anuncios)
    
    print(c)


    
