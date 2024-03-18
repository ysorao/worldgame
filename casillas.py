#Preguntas
'''Creamos una lista con preguntas, cada pregunta tiene 2 partes: 
    1. Pregunta que se realiza al jugador.
    2. Respuesta
'''
acertijos =[("Soy ligero como una pluma, pero ni el hombre más fuerte del mundo puede sostenerme por mucho tiempo. ¿Qué soy?", "respiración"),
        ("Cuanto más de esto hay, menos ves. ¿Qué es?", "oscuridad"),
        ("Siempre va delante de ti, pero nunca lo ves. ¿Qué es?", "futuro"),
        ("Se rompe antes de usarlo. ¿Qué es?", "huevo"),
        ("Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo rios y mares, pero no agua ni peces. ¿Qué soy?", "mapa"),
        ("Cuanto más le quitas, más grande se vuelve. ¿Qué es?", "hoyo"),
    ]

# Penalidad
'''la lista de penalidad contiene las casillas que son objeto de penalizaciones, si el jugador cae en alguna de ellas , se regresa  automaticamente 10 casillas
'''
penalidad=[23,31,60]

#premios
''' La lista de premio contiene aquellas casillas que en caso de ser visitadas por el jugador avanzará 10 posiciones de manera automati 
'''
premio=[6,20,51]

#Preguntas
preguntas = [3,12,13,22,45,50]



