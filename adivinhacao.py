import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print('Tentativa {1} de {0}'.format(total_tentativas, rodada))
        chute_str = input("Digite o seu número: ")
        chute = int(chute_str)
        print("Você digitou {:03d}.".format(chute, numero_secreto))


        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        pontos = pontos - abs(chute - numero_secreto)
        isIgual = numero_secreto == chute
        if isIgual:
            print("Você acertou")
            break
        else:
            isMaior = chute > numero_secreto
            isMenor = chute < numero_secreto
            if isMaior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif isMenor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
    print("O número secreto é {:03d}. Você fez {:d} pontos.\nFim do jogo!".format(numero_secreto, pontos))


if __name__ == "__main__":
    jogar()
