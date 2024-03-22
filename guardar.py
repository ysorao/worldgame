'''
La función guardar recibe los parametros: mombre de usuario y puntaje para guardarlos en el archivo txt y mantener el histórico. 
'''

def guardar_concursante(nombre, puntaje):
    with open("concursantes.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntaje}\n")