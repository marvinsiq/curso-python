import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

max_pontos = 1000;
pontos = 1000
rodada = 1
menor_numero = 1;
maior_numero = 100;
numero_secreto = random.randrange(menor_numero, maior_numero + 1);

print(numero_secreto);
print("\nTente adivinhar o número entre {} e {}".format(menor_numero, maior_numero))

print("Qual o nível de dificuldade?")
nivel = 0
while nivel != 1 and nivel != 2 and nivel != 3:
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

acertou = False

for rodada in range(1, total_de_tentativas + 1):

    print("\nTentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Palpite inválido. O número está entre {} e {}".format(menor_numero, maior_numero))
        continue

    if (chute == numero_secreto):
        print("Você acertou e fez {} pontos de um total de {}!".format(pontos, max_pontos))
        acertou = True
        break
    else:
        if (chute > numero_secreto):
            print("Você errou! Tente um número MENOR !")
        else:
            print("Você errou! Tente um número MAIOR !")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

if not acertou:
    print("Fim do Jogo. O número era {}.".format(numero_secreto))
else:
    print("Fim do Jogo.")