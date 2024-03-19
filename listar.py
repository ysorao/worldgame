from leerResultados import *


def listar_top_5():
    concursantes = leer_concursantes()
    concursantes.sort(key=lambda x: x[1], reverse=True)  # Ordenar por puntaje, de mayor a menor
    top_5 = concursantes[:5]
    print("***** Top 5 Concursantes *****")
    for i, (nombre, puntaje) in enumerate(top_5, start=1):
        print(f"{i}. {nombre} - {puntaje} puntos ")