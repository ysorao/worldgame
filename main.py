from tablero import *
from ubicacion import *
from tableroIni import *
from mensajes import *
from dado import *

# print("--------------------------------------------------\n--------------------------------------------------")
# print("--------------------------------------------------\n--------------------------------------------------")

print("********************************\n***        WORLD GAME        ***\n********************************")


# print(mensaje_bienvenida)
# tablero_inicial()

'''REcolectar  Nombre del usuario'''
usuario =  input("Ingresa tu nombre de usuario: ")

print(f"Bienvenido:  {usuario}")

'''Lanzamiento del  dado'''
input("Presiona Enter para lanzar el dado...")
resultado_dado = lanzar_dado()
print(f"Has lanzado un {resultado_dado}")


''' Asignación de la casilla'''
casillaJugador =0
casillaJugador += resultado_dado
nuevaUbicacion = coordTab[casillaJugador-1]
tablero_ubicacion(nuevaUbicacion)


# input(mensaje_inicio)
# coordenadas = (7,7)  # Coordenadas donde se colocará la inicial del jugador  o un identificador
# pintar_tablero(coordenadas)

