class Pelota():
    def __init__(self, color: str, tamanio: int, material: str):
        self.color = color
        self.tamanio = tamanio
        self.material = material

    def __init__(self, color="-", tamanio=0, material="-"):
        self.color = color
        self.tamanio = tamanio
        self.material = material

p = Pelota("Amarillo", 16, "plástico")
# Salida: Amarillo 16 plástico
print(p.color, p.tamanio, p.material)
# Salida:
# TypeError: __init__() missing 3 required positional arguments:
# 'color', 'tamanio', and 'material'
p2 = Pelota()
print(p2.color,p2.tamanio,p2.material)