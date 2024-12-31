import datetime
def idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento


def maioridade (nome, idade):
    if idade < 18:
        print(f"{nome} é menor de idade!")
    else:
        print(f"{nome} é maior de idade!")



nome = input(f"Digite o nome da pessoa: ")
ano_atual = int(input(f"Digite o ano atual: "))
ano_nascimento = int(input(f"Digite o ano de nascimento: "))

idade_pessoa = idade(ano_atual, ano_nascimento)
maioridade(nome, idade_pessoa)






