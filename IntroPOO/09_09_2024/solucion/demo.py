from campania import Campania
from error import LargoExcedidoException
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
             "sub_tipo":"instream",
             "ancho":220,
             "alto":200}
             ]
    
try:
    
    c = Campania("Campaña 1", date(2024,9,10),date(2024,9,17),anuncios)
    print(c)
    
    c.nombre = input("Nombre de la campaña (Max 250 c): ")
    print(c)

except LargoExcedidoException as ex:
    print(ex)
    crearLog("error.log", ex.mensaje)
