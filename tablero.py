def tablero_ubicacion(coordenadas):
    casillasTablero= [64,63,62,61,60,59,58,57,49,50,51,52,53,54,55,56,48,47,46,45,44,43,42,41,33,34,35,36,37,38,39,40,32,31,30,29,28,27,26,25,17,18,19,20,21,22,23,24,16,15,14,13,12,11,10,9,1,2,3,4,5,6,7,8]
    indice = 0
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
                        print(" ■ ", end="") # Ubicamos la posicion actual del jugador
                    else:
                        print("   ", end="")
            print("")  # Cierre de fila

coordenadas = (6, 5)  # Coordenadas donde se colocará la inicial del jugador  o un identificador
tablero_ubicacion(coordenadas)