class PelotaDePlastico():
    def __init__(self) -> None:
        self.rebotes = []

    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [int(altura), 0]
            altura //= 1.1

class PelotaDeJuguete(PelotaDePlastico):
    def rebotar(self, altura) -> None:
        self.rebotes = []
        while altura > 0:
            self.rebotes += [altura, 0]
           # print(self.rebotes)
            altura //= 2
            
pdj = PelotaDeJuguete()
pdj.rebotar(5)
# Salida: [5, 0, 1, 0]
print(pdj.rebotes)
# Se hace llamado al método del padre PelotaDePlastico
print(type(pdj))
super(type(pdj), pdj).rebotar(5)
# Salida: [5, 0, 2, 0, 1, 0]
print(pdj.rebotes)