from te import Te

sabor = int(input("¿Qué sabor de té desea? (Ingrese número de la opción)"
 "\n1. Té negro \n2. Té verde \n3. Té de hierbas\n"))

formato = int(input("¿Qué formato desea?. Tenemos disponible"
" 300 y 500 gramos. Ingrese la cantidad de gramos deseada\n"))

tiempo, recomendacion = Te.retorna_tiempo_y_recomendacion(sabor)
precio = Te.retorna_precio(formato)

if sabor == 1:
    sabor_texto = "Té negro"
elif sabor == 2:
    sabor_texto = "Té verde"
elif sabor == 3:
    sabor_texto = "Agua de hierbas"

print("Se ingresó su pedido de {}, en formato de {} gramos," 
"el cual tiene un valor de ${}. Este té tiene un tiempo "
"de preparación de {} minutos, y se recomienda su uso {}.".format(
    sabor_texto, formato, precio, tiempo, recomendacion
))
