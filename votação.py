X = 0
cebolinha = 0
gohan = 0
athena = 0
while X < 4: 
    print("========= VOTAÇÃO =========")
    print("1 - Cebolinha")
    print("2 - Gohan")
    print("3 - Athena")
    print("4 - Encerrar votação")
    X = int(input("Digite seu voto: "))
    if X == 1:
        cebolinha = cebolinha + 1
    elif X == 2:
        gohan = gohan + 1
    elif X == 3:
        athena = athena + 1
print("========= RESULTADO =========")
print("Candidato Cebolinha:", cebolinha)
print("Candidato Gohan:", gohan)
print("Candidato Athena:", athena)

total = cebolinha + gohan + athena
print("Total de votos:", total)
print("======================================")
if cebolinha > gohan and cebolinha > athena:
    print("Candidato Cebolinha vençeu as eleições")
elif gohan > cebolinha and gohan > athena:
    print("Candidato Gohan vençeu as eleições")
else:
    print("Candidato Athena vençeu as eleições")
print("======================================")


#Adicione o numero total de votos
# Adicione quem foi o vencedor 1º da eleição1
