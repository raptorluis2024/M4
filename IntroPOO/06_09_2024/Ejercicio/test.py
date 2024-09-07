import os
import time
from foto import Foto
from album import Album
from error import DimensionError
from util import crearLog

print(os.path.abspath(""))
ruta = os.path.abspath("ejercicio")
print("Creando Albun de fotos..")
time.sleep(1)
print("Album creado")
album = Album(nombre="First-Album")
print(album)
print("importando fotos")
time.sleep(1)

try:

    with open(ruta+"\\fotos.txt","r") as fotitos:
        linea = fotitos.readline()
      
        while linea:
            try:        
                ###cada linea es una foto
                f = linea.split(",")
                foto = Foto(int(f[0]),int(f[1]),f[2])
                if foto is not None:
                    print(foto)
                    album.addFoto(foto)
                linea = fotitos.readline()
            except DimensionError as de:
                print(de)
                crearLog("error.log",de)
                linea = fotitos.readline()
       
except Exception as e:
    print(e)
else:
    print("lectura de fotos realizada")
    time.sleep(1)
    
album.listar_fotos()

        
