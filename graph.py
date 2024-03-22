def tablero_inicial(ubicacion):
    casillasTablero= [64,63,62,61,60,59,58,57,49,50,51,52,53,54,55,56,48,47,46,45,44,43,42,41,33,34,35,36,37,38,39,40,32,31,30,29,28,27,26,25,17,18,19,20,21,22,23,24,16,15,14,13,12,11,10,9,1,2,3,4,5,6,7,8]
    indice = 0
    for fila in range(17):
        
        if fila % 2 == 0:  # Líneas horizontales
            print("+" + "-----+" * 8)
        else:  # Filas de casillas
            
            for columna in range(17):
                if columna % 2 == 0:  # Separadores verticales
                    print("|", end="")
                else:
                    # Ajustar las coordenadas para el tablero impreso ya que  tenemos casillas con un solo digito y casillas con dos digitos que generan desproporcion
                    if casillasTablero[indice] < 10:
                        if casillasTablero[indice] == ubicacion:
                            print("  ■ ", end=" ") #adicionar espacios para que el tablero se vea uniforme
                        else:
                            print(" ",casillasTablero[indice], " ", end="") #adicionar espacios para que el tablero se vea uniforme
                    else:
                        if casillasTablero[indice] == ubicacion:
                            print("  ■ ", end=" ") #adicionar espacios para que el tablero se vea uniforme
                        else:
                            print(" ",casillasTablero[indice], end=" ")

                    indice +=1
                    
            print("")  # Cierre de fila


tablero_inicial(64)