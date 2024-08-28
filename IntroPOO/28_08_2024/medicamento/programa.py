from medicamento import Medicamento

nombre = input("Ingrese nombre del medicamento:\n")
stock = int(input("Ingrese stock del medicamento:\n"))
precio_bruto = int(input("Ingrese precio bruto del medicamento:\n"))

m1 = Medicamento(nombre, stock)
m1.precio = precio_bruto
print(f"El precio bruto del medicamento {m1.nombre} es {m1.precio_bruto}")

if m1.descuento:
    print(f"Tiene un descuento de {m1.descuento * 100}%")

print(f"El precio final del medicamento es {m1.precio_final}")

