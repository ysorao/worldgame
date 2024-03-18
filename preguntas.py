import random

def acertijo_aleatorio(acertijos, preguntas_realizadas):
    if len(preguntas_realizadas) == len(acertijos):
        print("Ya has respondido a todos los acertijos.")
        return None, preguntas_realizadas

    while True:
        # Seleccionar un acertijo al azar
        indice_aleatorio = random.randint(0, len(acertijos) - 1)

        # Verificar si el acertijo ya ha sido utilizado
        if indice_aleatorio not in preguntas_realizadas:
            acertijo, respuesta = acertijos[indice_aleatorio]
            break

    # Pedir la respuesta al usuario
    respuesta_usuario = input(f"Acertijo: {acertijo}\nTu respuesta: ").lower().strip()

    # Agregar el índice del acertijo a las preguntas realizadas
    preguntas_realizadas.append(indice_aleatorio)

    correct = False

    # Verificar la respuesta
    if respuesta_usuario == respuesta:
        print("¡Correcto! Puedes avanzar")
        correct = True
    else:
        print(f"Incorrecto. La respuesta correcta era '{respuesta}'.")
        numeroIntentos -= numeroIntentos
        hacer_pregunta()

    return indice_aleatorio, preguntas_realizadas



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

preguntas_realizadas = []

# while len(preguntas_realizadas) < len(acertijos):
#     _, preguntas_realizadas = acertijo_aleatorio(acertijos, preguntas_realizadas)

def hacer_pregunta():
    global preguntas_realizadas


    if len(preguntas_realizadas) < len(acertijos):
        _, preguntas_realizadas = acertijo_aleatorio(acertijos, preguntas_realizadas)

