class Personaje:
    
    def __init__(self, nombre:str) -> None:
        self._nombre = nombre
        self._nivel = 1
        self._experiencia = 0
    
    @staticmethod
    def validar_nivel(valor):
        return valor >= 1
    
    @staticmethod
    def validar_experiencia(valor):
        return valor >= 0 and valor <= 99
    
    @property
    def estado(self):
        return f"Nombre {self.nombre}, Nivel {self.nivel} Experiencia {self.experiencia}"
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, valor):
        
        if not self.validar_nivel(valor):
            print("Error en el nivel")
        else:
            self._nivel = valor
        
    @property 
    def experiencia(self):
        return self._experiencia
    
    @experiencia.setter
    def experiencia(self, valor):
        if not self.validar_experiencia(valor):
            print("Error en la experiencia")
        else:
            self._experiencia = valor
    
    @estado.setter
    def estado(self, valor):
        
        exp_temp = self.experiencia + valor%100
        nivel_temp = self.nivel + valor//100
        print(self.nivel, nivel_temp,valor)
        self.nivel = nivel_temp 
        self.experiencia  = exp_temp   
     
    def __gt__(self, other):
        pass
    
    def __lt__(self, other):
        pass



if __name__ == "__main__":
    p = Personaje("prueba")
    print(p.estado)
    p.estado = 490
    print(p.estado)
    
