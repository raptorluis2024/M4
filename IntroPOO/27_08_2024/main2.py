# archivo generar_orden.py
from orden_compra import OrdenCompra

oc = OrdenCompra()
oc.nueva_orden()

oc.identificador = int(input("Ingrese identificador de la OC:\n"))

oc.total_productos = int(input("Ingrese total de productos:\n"))
monto = int(input("Ingrese monto:\n"))
oc.asigna_monto(monto)
print(oc.codigo_descuento)

