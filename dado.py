import random

def lanzar_dado():
    # Lanzar un dado de 6 caras
    resultado = random.randint(1, 6)
    return resultado

# Esperar a que el usuario presione Enter

'''
Esta función dibuja un dado en la consola indicando el numero obtenido despues de lanzarlo, recibe como parametro un valor  que corresponde al resultado de la función lanzar_dado() 
'''
def mostrar_dado(valor):
    print(f"  +---------+\n /         /|\n+---------+ |\n|         | |\n|    {valor}    | +\n|         |/\n+---------+\n")



