from datetime import datetime
def crearLog(archivo:str, mensaje:str):
    with open(archivo, "a+") as log:
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {mensaje}\n")


if __name__ == "__main__":
    crearLog("error.log", "mensaje de prueba")
    