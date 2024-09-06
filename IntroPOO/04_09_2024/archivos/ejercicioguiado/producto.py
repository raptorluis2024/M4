import json
import os
instancias = []

class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio
    def __str__(self) -> str:
        return f"Producto: {self.nombre} Precio :{self.precio}"
        
#print(os.path.abspath("archivos\\ejercicioguiado\\productos.txt"))
with open(os.path.abspath("archivos\\ejercicioguiado\\productos.txt")) as productos:
    linea = productos.readline()
    while linea:
        producto = json.loads(linea)
        print(producto, type(producto))
        instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
        linea = productos.readline()
for x in instancias:
    print(x)
        