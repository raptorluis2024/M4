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
       
        if valor < 0:
            nivel_tmp = self.nivel + valor//100
            print(f"{self.nombre} nivel temporal {nivel_tmp}")
            if nivel_tmp > 1:
                self.nivel = nivel_tmp
            exp_temp = self.experiencia + valor%100    
            print(f"{self.nombre} experiencia temporal {exp_temp}")
            if exp_temp > 0:   
                self.experiencia = exp_temp 
            print(self.nombre,valor, self.nivel, nivel_tmp, self.experiencia, exp_temp)
        else:
            exp_temp = self.experiencia + valor%100
            nivel_temp = self.nivel + valor//100
            self.nivel = nivel_temp 
            self.experiencia  = exp_temp 
            

    def get_probabilidad_ganar(self, other):
        print(self.nombre, self.nivel, other.nombre, other.nivel)
        if self < other:
            return 0.33       
        elif self > other:
            return 0.66
        else:
            return 0.5
    
    def __gt__(self, other):
        return self.nivel > other.nivel
    
    def __lt__(self, other):
        return self.nivel < other.nivel
    
    def __eq__(self, other):
        return self.nivel == other.nivel
    
    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(input(
            f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
            "de probabilidades de ganarle al Orco.\n"
            "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
            "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
            "\n¿Qué deseas hacer?\n"
            "1. Atacar\n"
            "2. Huir\n"
        ))


if __name__ == "__main__":
    p = Personaje("prueba")
    print(p.estado)
    p.estado = 490
    print(p.estado)
    
