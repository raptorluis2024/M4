from campania import Campania
from error import LargoExcedidoException,SubTipoInvalidoError
from log import crearLog
from datetime import date

anuncios = [{"tipo":"Video",
             "url_archivo":"http://www.campania2024.cl/archivo1.html",
             "url_click":"http://www.campania2024.cl",
             "duracion":100,
             "sub_tipo":"instream"},

             {"tipo":"Video",
             "url_archivo":"http://www.campania2024.cl/archivo2.html",
             "url_click":"http://www.campania2024.cl",
             "duracion":100,
             "sub_tipo":"instream"},

             {"tipo":"Display",
             "url_archivo":"http://www.campania2024.cl/archivo3.html",
             "url_click":"http://www.campania2024.cl",
             "sub_tipo":"tradicional",
             "ancho":220,
             "alto":200}
             ]
    
try:
    
    c = Campania("Campaña 1", date(2024,9,10),date(2024,9,17),anuncios)
    print(c)
    
    c.nombre = input("Nombre de la campaña (Max 250 c): ")
    print(c)
    
    tipo = input("Ingrese el nuevo tipo para el display de la campaña: ")
    c.getAnuncio(2).sub_tipo = tipo
    

except LargoExcedidoException as ex:
    print(ex)
    crearLog("error.log", ex.mensaje)
except SubTipoInvalidoError as err:
    print(err)
    crearLog("error.log", err.mensaje)
else:
    print("Datos procesados satisfactoriamente")
