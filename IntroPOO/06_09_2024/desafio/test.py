from usuario import Usuario
from util import crearLog
import os
import json
import time

usuarios=[]
def listarUsers(lista):
    print("Listado de usuarios")
    for x in lista:
        print(x)
        
contador = 1     
ruta = os.path.abspath("desafio")
try:
    with open(ruta+"\\usuarios.txt","r") as fotitos:
        linea = fotitos.readline()
        while linea:
            try:
                user = json.loads(linea)
                u = Usuario(user.get("nombre"),user.get("apellido"),user.get("email"),user.get("genero"))
                usuarios.append(u)
                contador += 1
                linea = fotitos.readline()
            except json.JSONDecodeError as e:
                crearLog(ruta+"\\error.log", f"Lectura fallida usuario linea {contador}, causa {e}")
                contador += 1
                linea = fotitos.readline()
        
except Exception as ex:
    print(ex)
else:
    crearLog(ruta+"\\error.log","proceso finalizado")
    time.sleep(1)
listarUsers(usuarios)
