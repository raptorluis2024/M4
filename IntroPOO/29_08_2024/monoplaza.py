#Clase principal
class Monoplaza:
    color = ""

    def aceleracion(self):
        print("El monoplaza acelera")
    def frenado(self):
        print("El monoplaza frena")

#Subclase que -->hereda<-- de la principal
class Redbull(Monoplaza):
    def aceleracion(self):
        print("El monoplaza Redbull acelera hasta los 450km/h")
    def frenado(self):
        print("El monoplaza Redbull tiene buena capacidad de frenado")
    def __str__(self):
        return("soy un redbull")
        
redbull = Redbull()
redbull.aceleracion()
redbull.frenado()
print(redbull)