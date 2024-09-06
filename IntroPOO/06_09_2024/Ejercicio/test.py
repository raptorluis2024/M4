import os
from foto import Foto
ruta = os.path.abspath("ejercicio")
try:

    with open(ruta+"\\fotos.txt","r") as fotitos:
        linea = fotitos.readline()
        while linea:
            print(linea)
            linea = fotitos.readline()
except Exception as e:
    print(e)
else:
    print("lectura de fotos realizada")
        
