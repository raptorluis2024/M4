from error import SubTipoInvalidoError
class Anuncio():
    def __init__(self, ancho:int, alto:int, url_archivo:str,url_click:str, sub_tipo:str ) -> None:
        self.__ancho = 1 if ancho < 0 else ancho
        self.__alto = 1 if alto < 0 else alto
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo
            
    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, alto:int):
        self.__alto = 1 if alto < 0 else alto
      
    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def alto(self, ancho:int):
        self.__alto = 1 if ancho < 0 else ancho
          
    @property
    def url_archivo(self):
        return self.__url_archivo
    @property 
    def url_click(self):
        return self.__url_click
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, subtipo):
             
        if subtipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Error:{self.__class__.__name__} No se puede cambiar el tipo") 
        else:
            self.__sub_tipo = subtipo
        
    @staticmethod
    def mostrar_formatos(instancia):
        if isinstance(instancia,Display):
            print("FORMATO DISPLAY")
            print("===============")
        elif isinstance(instancia,Video):
            print("FORMATO VIDEO")
            print("=============")
        elif isinstance(instancia,Social):
            print("FORMATO SOCIAL")
            print("==============")
            
        for f in instancia.SUB_TIPOS:
            print("-",f)
    
    def comprimir_anuncio(self):
        pass
    def redimensionar_anuncio(self):
        pass
    
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    
    def comprimir_anuncio(self):
        print("COMPRESION DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("RECORTE DE ANUNCIOS DISPLAY NO IMPLEMENTADO AUN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
            
    def comprimir_anuncio(self):
        print("COMPRESION DE ANUNCIOS REDES SOCIALES NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("RECORTE DE ANUNCIOS REDES SOCIALES NO IMPLEMENTADO AUN")

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, url_archivo: str, url_click: str, sub_tipo: str, duracion :int, ancho:int=1, alto:int=1 ) -> None:
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)
        self.__ancho = 1
        self.__alto = 1
        self.__duracion = duracion

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        if duracion > 0:
            self.__duracion = duracion 
        else:
            self.__duracion = 5
        
        
            
    def comprimir_anuncio(self):
        print("COMPRESION DE VIDEO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AUN")
    
    def mostrar_formatos(self):
        return super().mostrar_formatos(self)

if __name__ == "__main__":
    try:
        video = Video("url_archivo","url_click","instream",100)
        print(video.sub_tipo)
        Anuncio.mostrar_formatos(video)
        social = Social(100,100,"dsds","fdsfsdfsd","algo")
        Anuncio.mostrar_formatos(social)
        print(video.sub_tipo)
        video.sub_tipo = "prueba"
        print(video.sub_tipo)
    except SubTipoInvalidoError as ex:
        print(ex)
        
 
