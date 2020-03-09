print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1
menorNumero = 1;
maiorNumero = 100;


print("\nTente adivinhar o número entre {} e {}".format(menorNumero, maiorNumero))

for rodada in range(1, total_de_tentativas + 1):

    print("\nTentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Palpite inválido. O número está entre {} e {}".format(menorNumero, maiorNumero))
        continue

    if (chute == numero_secreto):
        print("Você acertou!")
        break
    elif (chute > numero_secreto):
        print("Você errou!\nTente um número MENOR !")
    else:
        print("Você errou!\nTente um número MAIOR !")

print("Fim do Jogo")