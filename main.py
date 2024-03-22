from tablero import *
from ubicacion import *
from tableroIni import *
from mensajes import *
from dado import *
from casillas import *
from preguntas import *
from guardar import *
from leerResultados import *
from listar import *

# Imprimir el nombre del juego
print(encabezado)

# imprime el top 5 de los mejores puntajes
listar_top_5()

# Imprime el mensaje de bienvenida y las instrucciones
print(mensaje_bienvenida)

# Imprime una muestra del tablero del juego
tablero_inicial()


# Ubicacion inicial
'''Variable  que almacena la posicion inicial del jugador'''
casillaJugador = 0

#Puntaje Jugador
'''Para dar inicio al juego se cargan 100 puntos'''
puntaje = 100


# usuario
'''Recolectar y almacenar Nombre del usuario'''
while True:
    usuario =  input("Ingresa tu nombre de usuario: ")
    if usuario =='' or len(usuario) < 5:
        print ("No puedes dejar el campo vacío, intenta nuevamente ingresando  un nombre o seudonimo con al menos 5 caracteres.")
    else:
        break


# Mensaje de saludo al Juagador    
print(f"Bienvenido:  {usuario}")


# Nivel de dificultad
'''
Se presentan las opciones de niveles de dificultad para que seleccione antes de iniciar el juego
'''
niveles = [1,2,3]

while True:
    try:
        nivel =  input(mensaje_niveles)
        if nivel.isdigit():
            nivel = int(nivel)
            if nivel in niveles:
                break
            else:
                print("Número fuera de rango. Por favor, elija un nivel entre 1, 2 o 3.")
        else:
            print("Entrada no válida. Por favor, ingrese un número entre 1,2 o 3.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entre 1,2 o 3.")

# Asignacion del nivel de dificultad
if nivel == 1:
    print(mensaje_dificultad_1)
elif nivel == 2:
    print(mensaje_dificultad_2)
elif nivel == 3:
    print(mensaje_dificultad_3)



# Oportunidades
'''Variable  que almacena el numero de intentos por partida, esta  variable  cambia de acuerdo con el nivel de dificultad seleccionado por el participante'''
if nivel ==1:
    oportunidades = 5
elif nivel == 2:
    oportunidades = 3
elif nivel == 3:
    oportunidades = 1



'''Inicio del Juego'''
def jugar():
    global nuevaUbicacion
    global casillaJugador
    global puntaje

    print ("Puntos: ", puntaje) # Se muestra el puntaje antes de lanzar el dado y avanzar

    input("Presiona Enter para lanzar el dado...") # lanzar el dado para obtener el numero de casillas a avanzar
    
    resultado_dado = lanzar_dado()
    mostrar_dado(resultado_dado)
    print(f"\nHas lanzado un {resultado_dado}\n")
    casillaJugador += resultado_dado    # Actualiza la casilla del jugador

    if casillaJugador > 64: # Valida si el jugador llegó al final del juego
        print(f"Solo te faltan {64 - (casillaJugador - resultado_dado)} casillas, debes lanzar de nuevo")
        casillaJugador -= resultado_dado
    elif casillaJugador == 64:
        bonus_preguntas = len(preguntas_realizadas) * 15
        puntaje = puntaje + bonus_preguntas 
        guardar_concursante(usuario, puntaje)
        print(f"El  Juego ha finalizado,  Muy bien!!, tu puntaje final es: {puntaje} " )
        print(mensaje_ganador)

                
    else:
        nuevaUbicacion = coordTab[casillaJugador-1]
        tablero_ubicacion(nuevaUbicacion)
        puntaje += resultado_dado

'''
el bucle casillaJugador se encarga de darle  continuidad al juego hasta que llegue a la casilla 64 o se terminen las oportunidades de respuesta
'''

while casillaJugador <= 63 : #se repite el ciclo hasta que el jugador finalice por oportunidades ==0 o por que llego a la casilla 64
    jugar()
    puntaje = puntaje -2
    
    tipoCasilla = validaCasillas(casillaJugador) # Recibe el tipo de casilla para generar las actividaes al jugador
    if tipoCasilla =="Pregunta":
        oportunidades_restantes = hacer_pregunta(oportunidades)
        oportunidades = oportunidades_restantes

        if oportunidades_restantes == 0: # Control de numero de oportunidades
            print(mensaje_perdedor)
            print("Puntos obtenidos: ",puntaje)
            break    

    elif tipoCasilla == "Premio":
        print("Avanzas 10 casillas de premio! , esta es tu nueva ubicacion")
        casillaJugador += 10 # Adiciona 10 posiciones al jugador como premio
        nuevaUbicacion = coordTab[casillaJugador-1]
        tablero_ubicacion(nuevaUbicacion)
        puntaje = puntaje + 10 # Aumenta el puntaje en 10 puntos 

    elif  tipoCasilla == "Penalidad":
        print("Lo siento! retrocede 10 casillas! , esta es tu nueva ubicacion")
        casillaJugador -= 10 # Resta 10 casillas  al jugador por penalizacion
        nuevaUbicacion = coordTab[casillaJugador-1]
        tablero_ubicacion(nuevaUbicacion)
        puntaje = puntaje - 10 # Resta 10 puntos  al jugador como penalidad
    






