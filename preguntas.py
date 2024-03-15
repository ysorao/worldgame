
def acertijos_y_respuestas():
    acertijos = [
        ("Soy ligero como una pluma, pero ni el hombre más fuerte del mundo puede sostenerme por mucho tiempo. ¿Qué soy?", "respiración"),
        ("Cuanto más de esto hay, menos ves. ¿Qué es?", "oscuridad"),
        ("Siempre va delante de ti, pero nunca lo ves. ¿Qué es?", "futuro"),
        ("Se rompe antes de usarlo. ¿Qué es?", "huevo"),
        ("Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo agua, pero no peces. ¿Qué soy?", "mapa"),
        ("Lo que te pertenece, otros lo usan más que tú. ¿Qué es?", "nombre"),
        ("Cuanto más le quitas, más grande se vuelve. ¿Qué es?", "hoyo"),
        ("Soy el principio del fin y el fin del tiempo y el espacio. Estoy en el medio de todas partes, pero no en ningún lugar en particular. ¿Qué soy?", "letra e"),
        ("¿Qué puede viajar por todo el mundo quedándose en una esquina?", "sello"),
        ("Puedo ser agarrado, pero nunca tirado. ¿Qué soy?", "pensamiento")
    ]

    puntaje = 0

    for acertijo, respuesta in acertijos:
        print(acertijo)
        respuesta_usuario = input("Tu respuesta: ").lower().strip()
        if respuesta_usuario == respuesta:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{respuesta}'.")

    print(f"\nTu puntaje final es {puntaje} de {len(acertijos)}.")

acertijos_y_respuestas()