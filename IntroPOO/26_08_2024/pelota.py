class Pelota():
    forma = "redondeada"
    posiciones = [3, 0, 2, 1, 0]
    
    @staticmethod
    def crear_rebote():
        return [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]  
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)