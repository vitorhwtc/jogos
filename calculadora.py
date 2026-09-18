X = 0
while X < 5:
    print("Calculadora")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - sair")

    X = int(input("Escolha a opção: "))
    
    if X == 1:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 + numero2
        print("Resultado:", resultado)
    elif X == 2:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 - numero2
        print("Resultado:", resultado)
    elif X == 3:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 * numero2
        print("Resultado:", resultado)
    elif X == 4:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 / numero2
        print("Resultado:", resultado)
