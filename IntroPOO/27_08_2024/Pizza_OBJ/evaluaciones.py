from pizza import Pizza

print("""Todas las pizzas tienen un precio de {} y un 
          tamaño {}""".format(Pizza.precio, Pizza.tamanio))
  

print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

p = Pizza()
p.inicializar_pizza()

p.realizar_pedido()
print("pizza valida" if p.validar_ingreso() else "pizza no valida")

