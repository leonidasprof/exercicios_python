def armazenar_nomes(nome_arquivo):
    with open(nome_arquivo, "w", encoding="UTF-8") as arquivo:
        for i in range(6):
            nome_completo = input("Digite o nome e sobrenome (separados por espaço:) ")
            arquivo.write(nome_completo + "\n")

def alterar_nomes(nome_arquivo):
    with open(nome_arquivo, "r+", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()
        arquivo.seek(0)
        arquivo.truncate()

        for linha in linhas:
            nome_completo = linha.strip()
            print(f"Nome atual: {nome_completo}")
            alterar = input("Deseja alterar (Sim/Não)? ").lower()

            if alterar == ("sim"):
                novo_nome = input("Digite o novo nome e sobrenome" )
                arquivo.write(novo_nome + "\n")
            else:
                arquivo.write(nome_completo + "\n")

nome_arquivo = "./nomes.txt"
armazenar_nomes(nome_arquivo)
alterar_nomes(nome_arquivo)
