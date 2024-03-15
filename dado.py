import random

def lanzar_dado():
    # Lanzar un dado de 6 caras
    resultado = random.randint(1, 6)
    return resultado

# Esperar a que el usuario presione Enter
input("Presiona Enter para lanzar el dado...")
resultado_dado = lanzar_dado()
print(f"Has lanzado un {resultado_dado}")
