
# archivo medicamento.py
class Medicamento():

    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    def asigna_precio(self, precio_entregado: int):
        es_valido = self.validar_mayor_a_cero(precio_entregado)
        if es_valido:
            self.precio = precio_entregado
            self.descuento = 0.0
            if self.precio >= 10000 and self.precio < 20000:
                self.descuento = 0.1
            elif self.precio >= 20000 and self.precio < 30000:
                self.descuento = 0.2
            elif self.precio >= 30000:
                self.descuento = 0.3
        else:
            print("El precio '{}' no es un precio válido".format(
            precio_entregado))
            self.precio=0
            self.descuento = 0