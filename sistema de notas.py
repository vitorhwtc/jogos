X = 0
nota = 0
situacao = "null"
while X < 3: 
    print("========= SISTEMA DE NOTAS =========")
    print("1 - Informar nota")
    print("2 - Consultar situação do aluno")
    print("3 - Sair")
    X = int(input("Escolha um opção: "))
    if X == 1:
        nota = int(input("Digite a nota do aluno: "))
        if nota < 0 or nota > 10:
            nota = 0
            print("Valor invalido.")
    elif X == 2:
        print("Nota:", nota)
        if nota >= 7:
            situacao = "Aprovado"
        if nota >= 5 and nota < 7:
            situacao = "Recuperação"
        if nota < 5:
            situacao = "Reprovado"
        print("Situação: ", situacao)