class Dato:
    def __init__(self, dato1):
        self.dato1 = dato1
        
    def __str__(self):
        return f"{self.dato1}"
       
    def __add__(self, suma_datos):
        return Dato(self.dato1 + suma_datos.dato1)
    
    def sumar(self, otro):
        return self.dato1 + otro.dato1
        
dato1 = Dato(10)
dato2 = Dato(30)
print(dato1 + dato2)
print(dato1)
print(dato1.sumar(dato2))

"""

    
    """