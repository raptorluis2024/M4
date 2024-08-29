class Tarjeta():
    def __init__(self, numero = "0000", cupo =0, serie=0) -> None:
        self._numero = numero
        self._cupo = cupo
        self._serie = serie
        
    @property
    def universal_code(self):
        return self._numero
    
    @universal_code.setter
    def universal_code(self, numero):
        if numero == "0001" or numero == "0000":
            raise ("Valor erróneo")
        self._numero = numero
        
    @property
    def detail(self):
        return f"Tarjeta {self._numero} cupo {self._cupo}"
    
t = Tarjeta()
print(t._cupo,t.universal_code,t._numero)
t.universal_code = "0002"
print(t.universal_code)
t.universal_code = "0009"
print(t.universal_code)
print(t.detail)
print(t.Detail())