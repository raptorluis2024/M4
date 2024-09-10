import os 
def crearLog(archivo, mensaje):
    ruta = os.path.abspath(f"solucion\\{archivo}")
    with open(ruta,"a+") as file:
        file.write(mensaje)
    file.close()


if __name__ == "__main__":
    crearLog("paso.log", "prueba\n")