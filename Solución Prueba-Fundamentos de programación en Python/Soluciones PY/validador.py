
def validate(opciones, eleccion):
    # Paso 1
    while eleccion not in opciones:
        # Paso 2
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] 
    # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no válidos a eleccion debe seguir preguntando
    validate(numeros, eleccion)