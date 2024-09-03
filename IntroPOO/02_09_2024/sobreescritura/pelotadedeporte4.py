##Parámetro especial **kwargs
class PelotaDeDeporte():
    def __init__(self, tamaño: int, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de deporte")
        self.tamaño = tamaño

class PelotaDePlastico():
    def __init__(self, material: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de plástico")
        self.material = material

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de ping pong")
        self.timbre = timbre

    def __str__(self):
        return f"{self.tamaño} {self.material} {self.timbre}"
 
class PelotaDeTennis(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, textura: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de tennis")
        self.textura = textura

    def __str__(self):
        return f"{self.tamaño} {self.material} {self.textura}"   
    
# Salida:
# Creando pelota de plástico
# Creando pelota de deporte
# Creando pelota de ping pong
pdpp = PelotaDePingPong(tamaño=4, material="celuloide",timbre="POWERTI")
print(pdpp)
pdt = PelotaDeTennis(tamaño=10, material="caucho", textura="rugosa")
print(pdt)