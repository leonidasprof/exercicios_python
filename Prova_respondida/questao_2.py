def votos():
    for i in range(10):
        print("--" * 20)
        votacao = int(input(f"{i+1}º Voto Digite (1) ou (2):"))
        votacoes.append(votacao)
        print("--" * 20)
    for num in votacao:
        if votacao != 0:
            votacao += 1
        else:
            print("Escolha (1) ou (2):")

            cont += 1

    with open("./votacao.txt", "w") as arquivo:
        arquivo.read("votacao.txt")
        qt_votos.append(arquivo)


votacoes = []
cont = 0
qt_votos = list()
votacao = 0
opcoes_votos = ["1- Star Wars", "2- Star Trek"]
print("--"*20)
print("       QUAL É A SUA OPÇÃO DE VOTO?")
print(f"\t{opcoes_votos}")
print("--"*20)
votos()
print(f"Quantidade de votos para Star Wars: {len(qt_votos[0])}")
print(f"Quantidade de votos para Star Trek: {len(qt_votos[1])}")
print("--"*20)

