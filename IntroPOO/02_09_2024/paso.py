class A():
    def __init__(self, algo:int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__algo = algo
    
    @property
    def algo(self):
        return self.__algo
    
    
class B(A):
    def __init__(self, algo:int, otracosa:str, **kwargs) -> None:
        super().__init__(algo, **kwargs) 
        self.__otracosa = otracosa

    @property
    def otracosa(self):
        return self.__otracosa
    
    def __str__(self) -> str:
        return f"{self.algo} {self.otracosa}"


paso = B(algo=10,otracosa="algo", porsiaca=100)
print(paso)
        