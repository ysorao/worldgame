import random

'''
Esta parte del código se encarga de las preguntas, dentro de las funcionalidades se encuentra que selecciones preguntas al azar, ingresar el indice de la pregunta seleccionada para que no se vuelva a repetir durante el juego, validar el numero de intentos de respuesta.
'''

def acertijo_aleatorio(acertijos, preguntas_realizadas, oportunidades):
    #contador de oportunidades, recibe  el parametro(número de oportunidades) que se asigna  donde se llama la  funcion, en este caso en elñ archivo main.py
    oportunidades = oportunidades
    print("oportunidades ", oportunidades)
    #pregunta si la  cantidad de preguntas realiozadas es igual a la cantidad de acertijos para  validar que ya se usaron todas las preguntas
    if len(preguntas_realizadas) == len(acertijos):
        print("Ya has respondido a todos los acertijos.")
        return

    # Seleccionar un acertijo al azar que no haya sido utilizado
    while True:
        indice_aleatorio = random.randint(0, len(acertijos) - 1)
        if indice_aleatorio not in preguntas_realizadas:
            acertijo, respuesta = acertijos[indice_aleatorio]
            break

    # Pedir la respuesta al usuario y repetir hasta acertar
    while oportunidades  > 0:
                
        respuesta_usuario = input(f"Acertijo: {acertijo}\nTu respuesta: ").lower().strip()
        if respuesta_usuario == respuesta:
            print("¡Correcto! Puedes avanzar")
            preguntas_realizadas.append(indice_aleatorio)
            break
        else:
            oportunidades = oportunidades - 1
            print(f"Incorrecto. te quedan {oportunidades} oportunidades. ")
        

def hacer_pregunta(oportunidades):
    global preguntas_realizadas
    
    if len(preguntas_realizadas) < len(acertijos):
        acertijo_aleatorio(acertijos, preguntas_realizadas,oportunidades)
        print (oportunidades)      
        

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

hacer_pregunta(3)




