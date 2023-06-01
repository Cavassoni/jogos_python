import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************")

    numero_secreto = round(random.randrange(1, 101))
    print(numero_secreto)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # while rodada <= total_de_tentativas:
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {} - pontos: {:4d}".format(rodada, total_de_tentativas, pontos))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou!")
            break
        else:
            if maior:
                print("Você errou! O seu chute", chute, " foi maior que o número secreto.")
            elif menor:
                print("Você errou! O seu chute ", chute, "foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo. Você fez {:4d} pontos".format(pontos))


if __name__ == "__main__":
    jogar()
