from tablero import *
from ubicacion import *
from tableroIni import *
from mensajes import *
from dado import *
from casillas import *
from preguntas import *


print(encabezado)
print(mensaje_bienvenida)
tablero_inicial()


#Oportunidades

oportunidades = 3
casillaJugador = 0

'''Recolectar y almacenar Nombre del usuario'''
usuario =  input("Ingresa tu nombre de usuario: ")
print(f"Bienvenido:  {usuario}")

'''Variable  que almacena el numero de intentos por partida'''
numeroIntentos = 3


'''Lanzamiento del  dado'''
def lanzarDado():
    global nuevaUbicacion
    global casillaJugador
    input("Presiona Enter para lanzar el dado...")
    resultado_dado = lanzar_dado()
    print(f"Has lanzado un {resultado_dado}")
    casillaJugador += resultado_dado
    nuevaUbicacion = coordTab[casillaJugador-1]
    tablero_ubicacion(nuevaUbicacion)



def validaCasillas(ubicacion):
    global tipoCasilla
    
    if ubicacion in preguntas:
        print("has caído en una casilla ", ubicacion,  " de tipo PREGUNTA")

        tipoCasilla="Pregunta"
    elif ubicacion in penalidad: 
        print("has caído en una casilla ", ubicacion,  " de tipo PENALIDAD")
        tipoCasilla= "Penalidad"
    elif ubicacion in premio:
        print("has caído en una casilla ", ubicacion,  " de tipo PREMIO")
        tipoCasilla= "Premio"
    else:
        print("has caído en una casilla ", ubicacion,  " de tipo VACÍA")
        tipoCasilla = 'Vacia'
    return tipoCasilla


while oportunidades  > 0 :
    lanzarDado()
    validaCasillas(casillaJugador)
    if tipoCasilla =="Pregunta":
        hacer_pregunta(3)
        
    elif tipoCasilla == "Premio":
        print("Avanzas 10 casillas de premio! , esta es tu nueva ubicacion")
        casillaJugador += 10
        nuevaUbicacion = coordTab[casillaJugador-1]
        tablero_ubicacion(nuevaUbicacion)
    elif  tipoCasilla=="Penalidad":
        print("Lo siento! retrocede 10 casillas de premio! , esta es tu nueva ubicacion")
        casillaJugador -= 10
        nuevaUbicacion = coordTab[casillaJugador-1]
        tablero_ubicacion(nuevaUbicacion)
    






# input(mensaje_inicio)
# coordenadas = (7,7)  # Coordenadas donde se colocará la inicial del jugador  o un identificador
# pintar_tablero(coordenadas)

