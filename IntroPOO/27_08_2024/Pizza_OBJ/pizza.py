from ingredientes import *

class Pizza():
    precio = 10000
    tamanio = "Familiar"
    
    @staticmethod
    def validar_elemento(elemento, lista):
        return elemento in lista
    
    
    def validar_ingreso(self):
        return self.validar_elemento(self.masa, masas) and \
        self.validar_elemento(self.proteico, proteicos) \
        and self.validar_elemento(self.ingredientes[0], vegetales) and self.validar_elemento(self.ingredientes[1], vegetales)
        
    
    def inicializar_pizza(self):
        self.ingredientes = []
        self.proteico = ""
        self.masa = ""
        self.valida = False
    
    def realizar_pedido(self):
        proteico = input("""Ingrese ingrediente proteico
                         Carne, Pollo Carne Vegetal  """).lower()
        self.proteico = proteico
        ingrediente1 = input("""Ingrese vegetal 1
                             tomate, aceitunas, champiñones""").lower()
        if ingrediente1 not in self.ingredientes:
            self.ingredientes.append(ingrediente1)
        
        ingrediente2 = input("""Ingrese vegetal 2
                             tomate, aceitunas, champiñones""").lower()
        if ingrediente2 not in self.ingredientes:
            self.ingredientes.append(ingrediente2)
        
        masa = input("""Ingrese masa tradicional, delgada""").lower() 
        self.masa = masa
        
        
    
    
    