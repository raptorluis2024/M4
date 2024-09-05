try:
    lista=[x for x in range(3)]
    dic = {"a":100, "b":200}
    n1 = int(input("ingrese un numero mayor a 10"))
    if n1 <= 10:
        raise ValueError("te dije que debia ser mayor a 10")
    n2 = int(input("ingrese otro numero"))
    print(n1+n2)
    print(dic["b"])
    print(lista[10])
except IndexError as ie:
    print("Error en el indice de acceso")
except KeyError:
    print("la clave no está en el diccionario")
except ValueError as ve:
    print(ve)
except Exception:
    print("oops")