import random

# Acertijos disponibles
acertijos = [
    ("Soy ligero como una pluma, pero ni el hombre más fuerte del mundo puede sostenerme por mucho tiempo. ¿Qué soy?", "respiración"),
    ("Cuanto más de esto hay, menos ves. ¿Qué es?", "oscuridad"),
    ("Siempre va delante de ti, pero nunca lo ves. ¿Qué es?", "futuro"),
    ("Se rompe antes de usarlo. ¿Qué es?", "huevo"),
    ("Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo rios y mares, pero no agua ni peces. ¿Qué soy?", "mapa"),
    ("Cuanto más le quitas, más grande se vuelve. ¿Qué es?", "hoyo"),
    ("Todo el día camino pero no me muevo de mi lugar, ¿que soy?", "reloj"),
    ("Te sigo todo el día, moviéndome con el sol, pero desaparezco en la noche. ¿Qué soy?", "sombra"),
    ("Cuanto más secas, más se moja. ¿Qué es?", "toalla"),
    ("Soy la única que estoy en todo y nada", "D"),
    ("¿Qué monte era el más alto del mundo antes de descubrir el Everest?", "everest")
]

# Preguntas ya realizadas
preguntas_realizadas = []

def hacer_pregunta(oportunidades):
    global preguntas_realizadas
    # Elegir una pregunta que no se haya hecho antes
    preguntas_disponibles = [acertijo for acertijo in acertijos if acertijo not in preguntas_realizadas]
    if not preguntas_disponibles:
        print("Ya se han realizado todas las preguntas.")
        return oportunidades

    pregunta, respuesta = random.choice(preguntas_disponibles)
    preguntas_realizadas.append((pregunta, respuesta))

    # Preguntar al usuario
    while oportunidades > 0:
        respuesta_usuario = input(pregunta + " ")
        if respuesta_usuario.lower() == respuesta:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto. Intenta de nuevo.")
            oportunidades -= 1

    return oportunidades

# Ejemplo de uso
oportunidades_restantes = hacer_pregunta(3)
print(f"Oportunidades restantes: {oportunidades_restantes}")