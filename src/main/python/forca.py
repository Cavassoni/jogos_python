import http.client
import json
import os
import random
from codecs import encode

from unidecode import unidecode

ajudas = 0


def jogar():
    imprime_mensagem_abertura()

    print("Buscando palavra secreta...")

    palavra_secreta, dica = carrega_palavra_secreta_web()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_erradas = []

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        exibir_dados(dica, erros, letras_acertadas, letras_erradas)
        chute = pede_chute(letras_acertadas, palavra_secreta)

        acertou = valida_finalizacao(acertou, letras_acertadas)

        if chute is None:
            continue

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            acertou = valida_finalizacao(acertou, letras_acertadas)
        else:
            letras_erradas.append(chute)
            erros += 1

        if erros == 7:
            enforcou = True
            imprime_mensagem_perdedor(palavra_secreta)


def valida_finalizacao(acertou, letras_acertadas):
    if "_" not in letras_acertadas:
        acertou = True
        imprime_mensagem_vencedor()
    return acertou


def exibir_dados(dica, erros, letras_acertadas, letras_erradas):
    os.system('clear')
    desenha_forca(erros)
    exibir_palavra(letras_acertadas)
    if len(letras_erradas) > 0:
        print("Letras erradas: {}".format(letras_erradas))

    if ajudas > 0:
        print("Ajudas: {}".format(ajudas))
    print(dica)


def exibir_palavra(letras_acertadas):
    for f in letras_acertadas:
        print(f, end=" ")
    print("\n")


def imprime_mensagem_perdedor(palavra_secreta):
    os.system('clear')
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
    os.system('clear')
    if ajudas <= 3:
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
    else:
        print("\n\nVocê ganhou, mas usou muitas ajudas! Nada de troféu para você!")


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


def preenche_letra(letras_acertadas, palavra_secreta):
    tamanho = len(palavra_secreta)

    while True:
        index = random.randrange(0, tamanho)
        if letras_acertadas[index] == "_":
            letra = palavra_secreta[index]

            letras_acertadas[index] = letra

            for (index, le) in enumerate(palavra_secreta):
                if le == letra:
                    letras_acertadas[index] = letra
            break


def pede_chute(letras_acertadas, palavra_secreta):
    chute = input("Informe uma letra (Digite 1 para ajuda): ")
    chute = chute \
        .strip() \
        .upper()
    if len(chute) > 1:
        print("Você deve digitar apenas uma letra!")
        return pede_chute(letras_acertadas, palavra_secreta)

    if chute.isnumeric():
        if chute == "1":
            global ajudas
            ajudas += 1
            preenche_letra(letras_acertadas, palavra_secreta)
            return
        print("Você deve digitar apenas letras!")
        return pede_chute(letras_acertadas, palavra_secreta)

    if not chute.isalpha():
        print("Você deve digitar apenas letras!")
        return pede_chute(letras_acertadas, palavra_secreta)

    return chute


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def carrega_palavra_secreta_arquivo():
    arquivo = open("/palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()


def carrega_palavra_secreta_web():
    aux = random.randrange(1, 5)

    word_type = {
        1: "fruta",
        2: "animal",
        3: "corpo",
        4: "profissao"
    }

    conn = http.client.HTTPSConnection("www.invertexto.com")
    data_list = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    data_list.append(encode('--' + boundary))
    data_list.append(encode('Content-Disposition: form-data; name=type;'))

    data_list.append(encode('Content-Type: {}'.format('text/plain;utf-8')))
    data_list.append(encode(''))

    data_list.append(encode(word_type[aux]))
    data_list.append(encode('--' + boundary))
    data_list.append(encode('Content-Disposition: form-data; name=num_words;'))

    data_list.append(encode('Content-Type: {}'.format('text/plain;utf-8')))
    data_list.append(encode(''))

    data_list.append(encode("1"))
    data_list.append(encode('--' + boundary + '--'))
    data_list.append(encode(''))
    body = b'\r\n'.join(data_list)
    headers = {
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/ajax/words.php", body, headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    palavra_secreta = unidecode(data['result'][0]['word'].upper())
    return palavra_secreta, "Dica: {} ({} letras)".format(word_type[aux], len(palavra_secreta))


def imprime_mensagem_abertura():
    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")


if __name__ == "__main__":
    jogar()
