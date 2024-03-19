def leer_concursantes():
    concursantes = []
    try:
        with open("concursantes.txt", "r") as archivo:
            for linea in archivo:
                nombre, puntaje = linea.strip().split(',')
                concursantes.append((nombre, int(puntaje)))
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo cuando se guarde el primer concursante.")
    return concursantes