#Preguntas
'''Creamos una lista con preguntas, cada pregunta tiene 2 partes: 
    1. Pregunta que se realiza al jugador.
    2. Respuesta
'''

# Penalidad
'''la lista de penalidad contiene las casillas que son objeto de penalizaciones, si el jugador cae en alguna de ellas , se regresa  automaticamente 10 casillas
'''
penalidad=[23,31,60]

#premios
''' La lista de premio contiene aquellas casillas que en caso de ser visitadas por el jugador avanzará 10 posiciones de manera automati 
'''
premio=[6,20,51]

#Preguntas
''' La lista de premio contiene aquellas casillas que generan preguntas  
'''
preguntas = [3,9,12,13,17,22,36,45,50,59]

ganador =[64]


'''
La  funcion validaCasillas recibe el parametro de la ubicacion actual del jugador y valida si esta en alguna de las listas de premio, penalizacion o pregunta
'''
def validaCasillas(ubicacion):
    global tipoCasilla
    
    if ubicacion in preguntas:
        print("\nHas caído en la casilla ", ubicacion,  " de tipo PREGUNTA")
        tipoCasilla="Pregunta"
    elif ubicacion in penalidad: 
        print("\nHas caído en la casilla ", ubicacion,  " de tipo PENALIDAD")
        tipoCasilla= "Penalidad"
    elif ubicacion in premio:
        print("\nHas caído en la casilla ", ubicacion,  " de tipo PREMIO")
        tipoCasilla= "Premio"
    elif ubicacion in ganador:
        print("\nHas llegado al final del Juego")
    else:
        print("\nHas caído en la casilla ", ubicacion,  " de tipo VACÍA")
        tipoCasilla = 'Vacia'
    return tipoCasilla