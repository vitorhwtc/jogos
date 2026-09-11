import random

print("Jogo Jokenpo!")
valor = 0
opcoes = ["Pedra", "Papel", "Tesoura", "Cola"]




while True:
    valor += 1
    if valor > 3:
        restart = input("Gostaria de jogar novamente? (S/N) ").upper()
        if restart == "S":
            valor = 1
        if restart != "S":
             break
    print("Turno", valor)
    jogador = str(input("Escolha entre Pedra, Papel, Tesoura ou Cola: ").capitalize())

    if jogador not in opcoes:
        print("Escolha errada tente novamente.")
        continue

    pc = random.choice(opcoes)
    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Empate!")

    elif jogador == "Pedra":
        if pc == "Tesoura":
            print("Você venceu!")
        elif pc == "Cola":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")

    elif jogador == "Papel":
        if pc == "Pedra":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")   

    elif jogador == "Tesoura":
        if pc == "Papel":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")

    elif jogador == "Cola":
        if pc == "Papel":
            print("Você venceu!")
        elif pc == "Tesoura":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
