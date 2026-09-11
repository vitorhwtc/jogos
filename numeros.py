import random

print("Jogo dos numeros!")
valor = 0
opcoes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

while True:
    valor += 1

    if valor > 3:
        restart = input("Gostaria de jogar novamente? (Sim/Nao) ").upper()

        if restart == "SIM":
            valor = 1

        if restart != "SIM":
            break

    print("Turno", valor)

    jogador = input("Escolha entre 1 a 10: ").capitalize()

    if jogador not in opcoes:
        print("Resposta ínvalida, tente novamente.")
        continue

    pc = random.choice(opcoes)
    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Você acertou!")
        valor = 100
    else:
        print("Você errou!")

