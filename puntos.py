def puntos_juego(puntaje):
    print(f"********************\n**  Puntos: {puntaje}  **\n********************")



def puntaje_final(puntaje):
    print(f"\n\n*****************************\n**  Tu puntaje final: {puntaje}  **\n*****************************")


def bonus_oportunidades(oportunidades, nivel):
    if nivel == 1:
        bonusOportunidades = oportunidades * 10
    elif nivel == 2:
        bonusOportunidades = oportunidades * 20
    elif nivel == 3:
        bonusOportunidades = oportunidades * 30
        
    return bonusOportunidades