''' Aquí debemos  listar todos los mensajes de la aplicación a fin de tener mas limpio el codigo en el area de ejecución
'''

encabezado ="\n********************************\n***        WORLD GAME        ***\n********************************\n"

mensaje_bienvenida = "\nBienvenido al concurso WORLD GAME, \n\nInstrucciones:\n\nEl juego consta de un tablero de 64 casillas las cuales se deben recorrer en orden, el objetivo del juego es llegar a la casilla 64 o llegar lo mas cerca posible para acumular mas puntos\n-Para avanzar de debe lanzar el dado, el sistema ubica al jugador automáticamente en la nueva posición y entregará instrucciones de acuerdo al tipo de  casilla.\n\n** Tipos de casilla **\n1. Casilla vacía: no contine actividades ni penalizaciones por lo cual se podrá lanzar el dado de nuevo para seguir avanzando.\n2. Casilla pregunta: para  poder continuar en el juego debe responder una pregunta, tiene 3 intentos, si los falla el juego terminará.\n3. Casilla Premio: al llegar a esta casilla avanza 10 posiciones adicionales\n4. Casilla Penalización: al llegar a esta casilla retrocede 10 posiciones.\n\n Así se vera tu tablero al iniciar:"

mensaje_inicio = "Si Quiere Iniciar el Juego ingrese Y o  N para salir: "

mensaje_final = "Lo sentimos, se superó el numero de intentos, este es el final del Juego "

mensaje_dificultad_1="\nHas seleccionado el Nivel de Dificultad Fácil, tienes 5 oportunidades para contestar las preguntas durante el juego y más casillas de PREMIO que te permitiran avanzar más rapido en el Juego.\n"

mensaje_dificultad_2="\nHas seleccionado el Nivel de Dificultad Medio, tienes 3 oportunidades para contestar las preguntas durante el juego.\n"

mensaje_dificultad_3="\nHas seleccionado el Nivel de Dificultad Dificil, tienes 1 oportunidad para contestar las preguntas durante el juego y las preguntas tienen un nivel de dificultad mayor\n"

mensaje_niveles = "\nSelecciona el nivel de dificultad, ingresa 1, 2 o 3 de acuerdo con la siguiente información:\n\n1 - Fácil: contiene mas intentos de respuestas y más casillas de Premio \n2 - Medio: Las casillas de premio disminuyen al igual que los intentos \n3 - Difícil: solo tienes 1 intento y las preguntas son mas complejas.\nIngresa tu seleccion: "