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


print(encabezado)

listar_top_5()

print(mensaje_bienvenida)

tablero_inicial()



# Ubicacion inicial
'''Variable  que almacena la posicion inicial del jugador'''
casillaJugador = 0

#Puntaje Jugador
puntaje = 100


# usuario
'''Recolectar y almacenar Nombre del usuario'''
while True:
    usuario =  input("Ingresa tu nombre de usuario: ")
    if usuario =='' or len(usuario) < 5:
        print ("No puedes dejar el campo vacío, intenta nuevamente ingresando  un nombre o seudonimo con al menos 5 caracteres.")
    else:
        break


# Mensaje    
print(f"Bienvenido:  {usuario}")


# Nivel de dificultad
niveles = [1,2,3]

while True:
    try:
        nivel =  input("\nSelecciona el nivel de dificultad, ingresa 1, 2 o 3 de acuerdo con la siguiente información:\n\n1 - Fácil: contiene mas intentos de respuestas y más casillas de Premio \n2 - Medio: Las casillas de premio disminuyen al igual que los intentos \n3 - Difícil: solo tienes 1 intento y las preguntas son mas complejas.\nIngresa tu seleccion: ")
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





'''Lanzamiento del  dado'''
def lanzarDado():
    global nuevaUbicacion
    global casillaJugador
    global puntaje
    print ("Puntos: ", puntaje)


    input("Presiona Enter para lanzar el dado...")
    resultado_dado = lanzar_dado()
    print(f"\nHas lanzado un {resultado_dado}\n")
    casillaJugador += resultado_dado
    
    if casillaJugador > 64:
        print(f"Solo te faltan {64 - (casillaJugador - resultado_dado)} casillas, debes lanzar de nuevo")
        casillaJugador -= resultado_dado
    elif casillaJugador == 64:
        print("El  Juego ha finalizado,  Muy bien!!")
        bonus = len(preguntas_realizadas) * 15
        puntaje = puntaje + bonus
        guardar_concursante(usuario, puntaje)
                
    else:
        nuevaUbicacion = coordTab[casillaJugador-1]
        tablero_ubicacion(nuevaUbicacion)
        puntaje += resultado_dado


'''
el bucle casillaJugador se encarga de darle  continuidad al juego hasta que llegue a la casilla 64 o se terminen las oportunidades de respuesta
'''

while casillaJugador <= 63 :
    lanzarDado()
    puntaje = puntaje -2
    
    tipoCasilla = validaCasillas(casillaJugador)
    if tipoCasilla =="Pregunta":
        oportunidades_restantes = hacer_pregunta(oportunidades)
        oportunidades = oportunidades_restantes

        if oportunidades_restantes == 0:
            print(mensaje_final)
            print("Puntos obtenidos: ",puntaje)
            break    
    elif tipoCasilla == "Premio":
        print("Avanzas 10 casillas de premio! , esta es tu nueva ubicacion")
        casillaJugador += 10
        nuevaUbicacion = coordTab[casillaJugador-1]
        tablero_ubicacion(nuevaUbicacion)
        puntaje = puntaje +10
    elif  tipoCasilla == "Penalidad":
        print("Lo siento! retrocede 10 casillas! , esta es tu nueva ubicacion")
        casillaJugador -= 10
        nuevaUbicacion = coordTab[casillaJugador-1]
        tablero_ubicacion(nuevaUbicacion)
        puntaje = puntaje - 10
    

