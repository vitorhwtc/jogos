X = 0
add = 0
saldo = float(2000)
while X <= 3: 
    print(" CAIXA ELETRÔNICO")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    X = int(input("Escolha um opção: "))
    if X == 1:
            print("Saldo atual: R$", saldo)
    elif X == 2:
        add += float(input("Digite o valor do depósito (R$): "))
        if add > 0:
            saldo += add
            add = 0
        else:
            print("O deposito tem que ser maior que R$ 0")
    elif X == 3:
        add += float(input("Digite o valor do saque (R$): "))
        if add > 0:
            if saldo > add:
                saldo -= add
                add = 0
            else:
                print("Saldo insuficiente")
        else:
            print("O saque tem que ser maior que R$ 0")