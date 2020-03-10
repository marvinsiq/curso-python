from forca import forca
from adivinhacao import adivinhacao

def escolhe_jogo():

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Escolha o seu jogo: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()