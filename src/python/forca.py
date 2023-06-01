import os
import random


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_erradas = []

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pede_chute()
        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            letras_erradas.append(chute)
            erros += 1

        if erros == 7:
            enforcou = True
            desenha_forca(erros)
            imprime_mensagem_perdedor(palavra_secreta)
        elif "_" not in letras_acertadas:
            acertou = True
            imprime_mensagem_vencedor()
            print(letras_acertadas)
        else:
            print('\n' * 100)
            desenha_forca(erros)
            if len(letras_erradas) > 0:
                print("Letras erradas: {}".format(letras_erradas))
            print(letras_acertadas)


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 0:
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |    >--|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |    >--|--< ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |    >--|--< ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |    >--|--< ")
        print(" |       |    ")
        print(" |     _/     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |    >--|--< ")
        print(" |       |    ")
        print(" |     _/ \_  ")

    print(" |            ")
    print("_|___         ")
    print()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute \
        .strip() \
        .upper()
    return chute


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def carrega_palavra_secreta():
    arquivo = open("/home/cavassoni/Repositorios/cursos/jogos/src/resources/palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()


def imprime_mensagem_abertura():
    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")


if __name__ == "__main__":
    jogar()
