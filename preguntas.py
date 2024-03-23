import random

# Acertijos disponibles Nivel 1
acertijos_1 = [
    ("Soy ligero como una pluma, pero ni el hombre más fuerte del mundo puede sostenerme por mucho tiempo. ¿Qué soy?:", "Respiración"),
    ("Cuanto más de esto hay, menos ves. ¿Qué es?:", "Oscuridad"),
    ("Siempre va delante de ti, pero nunca lo ves. ¿Qué es?:", "Futuro"),
    ("Se rompe antes de usarlo. ¿Qué es?:", "Huevo"),
    ("Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo rios y mares, pero no agua ni peces. ¿Qué soy?:", "Mapa"),
    ("Cuanto más le quitas, más grande se vuelve. ¿Qué es?:", "Hoyo"),
    ("Todo el día camino pero no me muevo de mi lugar, ¿que soy?:", "Reloj"),
    ("Te sigo todo el día, moviéndome con el sol, pero desaparezco en la noche. ¿Qué soy?:", "Sombra"),
    ("Cuanto más secas, más se moja. ¿Qué es?:", "Toalla"),
    ("¿Qué monte era el más alto del mundo antes de descubrir el Everest?:", "Everest")
]


# Acertijos disponibles Nivel 2

acertijos_2=[
    ("Capital de Alemania:", "Berlin"),
    ("Capital de Francia:","Paris"),
    ("Capital de España:","Madrid"),
    ("Capital de Japón:","Tokio"),
    ("Capital de Australia:","Canberra"),
    ("Capital de Canada:","Otawa"),
    ("Capital de Brasil:","Brasilia"),
    ("Capital de Reino Unido:","Londres"),
    ("Capital de Suecia:","Estocolmo"),
    ("Capital de Grecia:","Atenas"),
    ("Capital de Portugal:","Lisboa"),
    ("Capital de Finlandia:","Helsinki"),
    ("Capital de Corea del Sur:", "Seul"),
    ("Capital de Vietnam:","Hanoi"),
    ("Capital de Nigeria:","Abuja"),
    ("Capital de Noruega:","Oslo")
]

# Acertijos disponibles Nivel 2

acertijos_3=[
    ("capital de Alemania:", "Berlin"),
    ("Capital de Francia:","Paris"),
    ("Capital de España:","Madrid"),
    ("Capital de Japón:","Tokio"),
    ("Capital de Australia","Canberra"),
    ("Capital de Canada:","Otawa"),
    ("Capital de Brasil:","Brasilia"),
    ("Capital de Reino Unido:","Londres"),
    ("Capital de Suecia:","Estocolmo"),
    ("Capital de Grecia:","Atenas"),
    ("Capital de Portugal:","Lisboa"),
    ("Capital de Finlandia:","Helsinki"),
    ("Capital de Corea del Sur:", "Seul"),
    ("Capital de Vietnam:","Hanoi"),
    ("Capital de Nigeria:","Abuja"),
    ("Capital de Noruega:","Oslo"),
    ("Soy ligero como una pluma, pero ni el hombre más fuerte del mundo puede sostenerme por mucho tiempo. ¿Qué soy?:", "Respiración"),
    ("Cuanto más de esto hay, menos ves. ¿Qué es?:", "Oscuridad"),
    ("Siempre va delante de ti, pero nunca lo ves. ¿Qué es?:", "Futuro"),
    ("Se rompe antes de usarlo. ¿Qué es?:", "Huevo"),
    ("Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo rios y mares, pero no agua ni peces. ¿Qué soy?:", "Mapa"),
    ("Cuanto más le quitas, más grande se vuelve. ¿Qué es?:", "Hoyo"),
    ("Todo el día camino pero no me muevo de mi lugar, ¿que soy?:", "Reloj"),
    ("Te sigo todo el día, moviéndome con el sol, pero desaparezco en la noche. ¿Qué soy?:", "Sombra"),
    ("Cuanto más secas, más se moja. ¿Qué es?:", "Toalla"),
    ("¿Qué monte era el más alto del mundo antes de descubrir el Everest?:", "Everest")
]



# Preguntas ya realizadas
preguntas_realizadas = []

def hacer_pregunta(oportunidades, nivel):
    if nivel == 1:
        acertijos = acertijos_1
    elif nivel == 2:
        acertijos = acertijos_2
    elif nivel == 3:
        acertijos = acertijos_3

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
        if respuesta_usuario.lower() == respuesta.lower():  #  Convertimos textos a minúsculas para evitar errores en la comparación
            print("\n¡Correcto!\n")
            break
        else:
            if oportunidades >=1:  # Validamos que aun tengamos  oportunidades en el Juego
                oportunidades -= 1 # Restamos oportunidades ya que la respuesta  en esta  parte de la validacion es incorrecta 
                print(f"\nIncorrecto. Quedan {oportunidades} oportunidades.\n") #imprime  mensaje de oportunidades 
                

    return oportunidades # Retorna  al modulo principal el numero de oportunidades para  saber si aun puede continuar en el Juego