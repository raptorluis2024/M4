import os
os.system("cls")
ruta = os.path.abspath("")

print("ruta", ruta)
#archivo = open(os.path.abspath("archivos/logs/error.log"))
#lineas = archivo.readlines()
#print(lineas)

archivo = open(os.path.abspath("archivos/productos.txt"))
lineas = archivo.readlines()
print(lineas)