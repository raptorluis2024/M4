import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Paso 8
    print(f'{enunciado[0]}\n')
    letras = ['A','B','C','D']
    for l,a in zip(letras, alternativas):
        print(f'{l}. {a[0]}')
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4
