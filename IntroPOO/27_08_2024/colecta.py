class Colecta():
    recaudacion = 0
    
    def crear_colecta(self):
        self.recaudacion = 0
        self.id = ""
    
    def aporte(self, monto:int):
        self.recaudacion += monto
        
    def mostrarAporte(self):
        print("mi recaudacion es ", self.recaudacion)
    
    @staticmethod    
    def recaudar(monto:int):
        Colecta.recaudacion += monto
        
c1 = Colecta()
c1.crear_colecta()
print(c1)
c2 = Colecta()
c2.crear_colecta()
micolecta = [c1,c2]
micolecta[0].aporte(1000)
micolecta[1].aporte(10000)
micolecta[0].aporte(1000)

for c in micolecta:
    c.mostrarAporte()
    Colecta.recaudar(c.recaudacion)
print(Colecta.recaudacion)
    
    