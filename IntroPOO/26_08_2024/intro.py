from medicamento import Medicamento
import pelota as p

miPelota = p.Pelota()
print(miPelota.forma, type(miPelota))

med1 = Medicamento()
med2 = Medicamento()
print(med1.descuento, med1.IVA,med2.IVA)
print(med1, med2)
med1 = med2
print(med1, med2)
print(p.Pelota.crear_rebote())
p.Pelota.imprimir_posiciones()