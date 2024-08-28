class Pelota():
    def __init__(self, color="Blanco", tamano=20, material="Plástico"):
        self._color = color
        self._tamano = max(1, tamano)
        self._material = material
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, valor):
        if not valor:
            raise ValueError("El color no puede estar vacío")
        self._color = valor

    @property
    def tamano(self):
        return self._tamano
    @tamano.setter
    def tamano(self, valor):
        if valor < 1:
            raise ValueError("El tamaño debe ser al menos 1")
        self._tamano = valor

    @property
    def material(self):
        return self._material
    
    @material.setter
    def material(self, valor):
        if not valor:
            raise ValueError("El material no puede estar vacío")
        self._material = valor

    @property
    def descripcion(self):
        return f"Pelota {self._color} de {self._material}, tamaño {self._tamano}"

# Uso de la clase mejorada
p = Pelota("Amarillo", 25, "plástico")
print(p.descripcion) # Salida esperada: "Pelota Amarillo de plástico, tamaño 25"
p.tamano = 0 # Esto generará ValueError

p = Pelota()

