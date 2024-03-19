def tablero_ubicacion(coordenadas):
    for fila in range(17):
        if fila % 2 == 0:  # Líneas horizontales
            print("+" + "---+" * 8)
        else:  # Filas de casillas
            for columna in range(17):
                if columna % 2 == 0:  # Separadores verticales
                    print("|", end="")
                else:
                    # Ajustar las coordenadas para el tablero impreso
                    if fila == coordenadas[0] * 2 + 1 and columna == coordenadas[1] * 2 + 1:
                        print(" X ", end="")
                    else:
                        print("   ", end="")
            print("|")  # Cierre de fila

# coordenadas = (0, 0)  # Coordenadas donde se colocará la inicial del jugador  o un identificador
# tablero_ubicacion(coordenadas)