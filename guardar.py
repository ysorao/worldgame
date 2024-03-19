def guardar_concursante(nombre, puntaje):
    with open("concursantes.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntaje}\n")