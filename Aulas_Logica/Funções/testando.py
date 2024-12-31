import pandas as pd
import requests

# Dados de atividades radicais por região em Pernambuco
atividades_pernambuco = {
    "Fernando de Noronha": [
        {"nome": "Mergulho", "descricao": "Explore o fundo do mar com uma rica diversidade de vida marinha.",
         "curiosidade": "Considerado o melhor local de mergulho no Brasil.",
         "dias": "Segunda a Domingo", "horarios": "8h às 17h", "valor": 200, "restricao": "Necessário saber nadar."},
        {"nome": "Voo Livre", "descricao": "Voe sobre as belas paisagens de Fernando de Noronha.",
         "curiosidade": "Vista deslumbrante da ilha do alto.",
         "dias": "Quarta a Domingo", "horarios": "9h às 16h", "valor": 300, "restricao": "Altura mínima de 1,5m."}
    ],
    "Porto de Galinhas": [
        {"nome": "Passeio de Buggy", "descricao": "Passeio pelas praias e dunas de Porto de Galinhas.",
         "curiosidade": "Roteiro que passa por 4 praias diferentes.",
         "dias": "Diariamente", "horarios": "9h às 18h", "valor": 150, "restricao": "Recomendado para todas as idades."}
    ],
    "Ilha de Itamaracá": [
        {"nome": "Canoagem", "descricao": "Remada por águas tranquilas ao redor da ilha.",
         "curiosidade": "Excelente para iniciantes em canoagem.",
         "dias": "Sábado e Domingo", "horarios": "8h às 12h", "valor": 80, "restricao": "Idade mínima de 10 anos."}
    ]
}


# Função para carregar dados dos arquivos Excel, se existirem
def carregar_dados():
    try:
        usuarios = pd.read_excel('usuarios.xlsx')
    except FileNotFoundError:
        usuarios = pd.DataFrame(columns=["usuario", "senha", "preferencias"])
    try:
        atividades = pd.read_excel('atividades.xlsx')
    except FileNotFoundError:
        atividades = pd.DataFrame(columns=["codigo", "nome", "localizacao", "dificuldade", "clima"])
    try:
        rotas = pd.read_excel('rotas.xlsx')
    except FileNotFoundError:
        rotas = pd.DataFrame(columns=["usuario", "atividades"])
    return usuarios, atividades, rotas


# Função para salvar dados nos arquivos Excel
def salvar_dados():
    usuarios.to_excel('usuarios.xlsx', index=False)
    atividades.to_excel('atividades.xlsx', index=False)
    rotas.to_excel('rotas.xlsx', index=False)


# Carregar dados ao iniciar o aplicativo
usuarios, atividades, rotas = carregar_dados()


# Função para registrar novo usuário
def registrar_usuario():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    preferencias = escolher_preferencias()
    global usuarios
    novo_usuario = pd.DataFrame({"usuario": [usuario], "senha": [senha], "preferencias": [", ".join(preferencias)]})
    usuarios = pd.concat([usuarios, novo_usuario], ignore_index=True)
    print("Usuário registrado com sucesso!")


# Função para escolher preferências a partir de um menu
def escolher_preferencias():
    opcoes = [
        "Rapel", "Stand Up Paddle", "Passeio de Buggy", "Mergulho", "Trekking",
        "Arvorismo", "Kite Surf", "Canoagem", "Tirolesa", "Escalada",
        "Mountain Bike", "Caiaque", "Voo Livre", "Canyoning"
    ]
    print("\nSuas preferências radicais:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

    escolhas = input("\nEscolha suas atividades preferidas separando os números por vírgula (ex: 1, 4, 7): ")
    indices = [int(num.strip()) - 1 for num in escolhas.split(',') if num.strip().isdigit()]
    preferencias = [opcoes[i] for i in indices if 0 <= i < len(opcoes)]
    return preferencias


# Função para fazer login
def fazer_login():
    global usuario
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if ((usuarios['usuario'] == usuario) & (usuarios['senha'] == senha)).any():
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha incorretos!")
        return False


# Função para exibir uma imagem relacionada ao passeio
def exibir_imagem_atividade(nome_atividade):
    print(f"\nExibindo imagem de {nome_atividade}...")
    url_imagem = f"https://exemplo.com/imagens/{nome_atividade.replace(' ', '_').lower()}.jpg"
    print(f"Link para imagem: {url_imagem}\n")


# Função para pesquisar atividades radicais por localização em Pernambuco
def pesquisar_atividades():
    print("--" * 30)
    print("Locais disponíveis para atividades radicais em Pernambuco:")
    print("--" * 30)
    for index, local in enumerate(atividades_pernambuco.keys(), start=1):
        print(f"{index}. {local}")

    escolha_local = int(input("\nEscolha um local (número): "))
    local_selecionado = list(atividades_pernambuco.keys())[escolha_local - 1]
    atividades = atividades_pernambuco[local_selecionado]

    print(f"\nAtividades disponíveis em {local_selecionado}:")
    for index, atividade in enumerate(atividades, start=1):
        print(f"{index}. {atividade['nome']}")

    escolha_atividade = int(input("Escolha uma atividade (número): "))
    atividade_selecionada = atividades[escolha_atividade - 1]

    # Exibindo detalhes da atividade selecionada
    print(f"\n--- {atividade_selecionada['nome']} ---")
    print(f"Descrição: {atividade_selecionada['descricao']}")
    print(f"Curiosidade: {atividade_selecionada['curiosidade']}")
    print(f"Dias disponíveis: {atividade_selecionada['dias']}")
    print(f"Horários: {atividade_selecionada['horarios']}")
    print(f"Valor: R$ {atividade_selecionada['valor']:.2f}")
    print(f"Restrições: {atividade_selecionada['restricao']}")
    exibir_imagem_atividade(atividade_selecionada['nome'])


# Função para exibir o dashboard personalizado
def exibir_dashboard():
    while True:
        print("--" * 20)
        print(f"\tOlá {usuario}, bem vindo a Nômade!\n No que podemos te ajudar?")
        print("--" * 20)
        print("1. Pesquisar Atividades Radicais")
        print("2. Planejar Roteiro")
        print("3. Ofertas e Descontos")
        print("4. Experiências Próximas")
        print("5. Acessar Perfil e Histórico")
        print("6. Buscar Hospedagem")
        print("--" * 20)
        escolha = input("Digite o número do que deseja fazer: ")
        print("--" * 20)

        if escolha == '1':
            pesquisar_atividades()
        elif escolha == '2':
            planejar_roteiro()
        elif escolha == '3':
            ofertas_descontos()
        elif escolha == '4':
            experiencias_proximas()
        elif escolha == '5':
            acessar_perfil()
        elif escolha == '6':
            buscar_hospedagem()
        else:
            print("Opção inválida!")
        print("--" * 20)
        if input("Deseja voltar ao menu principal? (s/n): ").lower() == 'n':
            break


# Função para planejar roteiro
def planejar_roteiro():
    print("\nPlanejar Roteiro")
    atividades_selecionadas = input("Digite os códigos das atividades selecionadas separados por vírgula: ").split(',')
    global rotas
    rotas = rotas.append({"usuario": usuario, "atividades": atividades_selecionadas}, ignore_index=True)
    print("Roteiro gerado com sucesso!")
    if input("Deseja compartilhar o roteiro com amigos por e-mail? (s/n): ").lower() == 's':
        email = input("Digite o e-mail do seu amigo: ")
        print(f"Roteiro enviado para {email} com sucesso!")


# Funções esboço para funcionalidades adicionais
def ofertas_descontos():
    print("Funcionalidade de Ofertas e Descontos ainda em desenvolvimento.")


def experiencias_proximas():
    print("Funcionalidade de Experiências Próximas ainda em desenvolvimento.")


def acessar_perfil():
    print("Funcionalidade de Perfil e Histórico ainda em desenvolvimento.")


def buscar_hospedagem():
    print("Funcionalidade de Hospedagem ainda em desenvolvimento.")


# Execução do programa
if __name__ == "__main__":
    print("Bem-vindo ao sistema Nômade Adventure!")
    if fazer_login():

Você
disse:
está
incompleto!
O
ChatGPT
disse:
ChatGPT
Aqui
está
o
código
completo
com as funções
renovadas
e
a
execução
do
programa
corrigido:

Pitão

Copiar
código
import pandas as pd
import requests

# Dados de atividades radicais por região em Pernambuco
atividades_pernambuco = {
    "Fernando de Noronha": [
        {"nome": "Mergulho", "descricao": "Explore o fundo do mar com uma rica diversidade de vida marinha.",
         "curiosidade": "Considerado o melhor local de mergulho no Brasil.",
         "dias": "Segunda a Domingo", "horarios": "8h às 17h", "valor": 200, "restricao": "Necessário saber nadar."},
        {"nome": "Voo Livre", "descricao": "Voe sobre as belas paisagens de Fernando de Noronha.",
         "curiosidade": "Vista deslumbrante da ilha do alto.",
         "dias": "Quarta a Domingo", "horarios": "9h às 16h", "valor": 300, "restricao": "Altura mínima de 1,5m."}
    ],
    "Porto de Galinhas": [
        {"nome": "Passeio de Buggy", "descricao": "Passeio pelas praias e dunas de Porto de Galinhas.",
         "curiosidade": "Roteiro que passa por 4 praias diferentes.",
         "dias": "Diariamente", "horarios": "9h às 18h", "valor": 150, "restricao": "Recomendado para todas as idades."}
    ],
    "Ilha de Itamaracá": [
        {"nome": "Canoagem", "descricao": "Remada por águas tranquilas ao redor da ilha.",
         "curiosidade": "Excelente para iniciantes em canoagem.",
         "dias": "Sábado e Domingo", "horarios": "8h às 12h", "valor": 80, "restricao": "Idade mínima de 10 anos."}
    ]
}


# Função para carregar dados dos arquivos Excel, se existirem
def carregar_dados():
    try:
        usuarios = pd.read_excel('usuarios.xlsx')
    except FileNotFoundError:
        usuarios = pd.DataFrame(columns=["usuario", "senha", "preferencias"])
    try:
        atividades = pd.read_excel('atividades.xlsx')
    except FileNotFoundError:
        atividades = pd.DataFrame(columns=["codigo", "nome", "localizacao", "dificuldade", "clima"])
    try:
        rotas = pd.read_excel('rotas.xlsx')
    except FileNotFoundError:
        rotas = pd.DataFrame(columns=["usuario", "atividades"])
    return usuarios, atividades, rotas


# Função para salvar dados nos arquivos Excel
def salvar_dados():
    usuarios.to_excel('usuarios.xlsx', index=False)
    atividades.to_excel('atividades.xlsx', index=False)
    rotas.to_excel('rotas.xlsx', index=False)


# Carregar dados ao iniciar o aplicativo
usuarios, atividades, rotas = carregar_dados()


# Função para registrar novo usuário
def registrar_usuario():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    preferencias = escolher_preferencias()
    global usuarios
    novo_usuario = pd.DataFrame({"usuario": [usuario], "senha": [senha], "preferencias": [", ".join(preferencias)]})
    usuarios = pd.concat([usuarios, novo_usuario], ignore_index=True)
    print("Usuário registrado com sucesso!")


# Função para escolher preferências a partir de um menu
def escolher_preferencias():
    opcoes = [
        "Rapel", "Stand Up Paddle", "Passeio de Buggy", "Mergulho", "Trekking",
        "Arvorismo", "Kite Surf", "Canoagem", "Tirolesa", "Escalada",
        "Mountain Bike", "Caiaque", "Voo Livre", "Canyoning"
    ]
    print("\nSuas preferências radicais:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

    escolhas = input("\nEscolha suas atividades preferidas separando os números por vírgula (ex: 1, 4, 7): ")
    indices = [int(num.strip()) - 1 for num in escolhas.split(',') if num.strip().isdigit()]
    preferencias = [opcoes[i] for i in indices if 0 <= i < len(opcoes)]
    return preferencias


# Função para fazer login
def fazer_login():
    global usuario
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if ((usuarios['usuario'] == usuario) & (usuarios['senha'] == senha)).any():
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha incorretos!")
        return False


# Função para exibir uma imagem relacionada ao passeio
def exibir_imagem_atividade(nome_atividade):
    print(f"\nExibindo imagem de {nome_atividade}...")
    url_imagem = f"https://exemplo.com/imagens/{nome_atividade.replace(' ', '_').lower()}.jpg"
    print(f"Link para imagem: {url_imagem}\n")


# Função para pesquisar atividades radicais por localização em Pernambuco
def pesquisar_atividades():
    print("--" * 30)
    print("Locais disponíveis para atividades radicais em Pernambuco:")
    print("--" * 30)
    for index, local in enumerate(atividades_pernambuco.keys(), start=1):
        print(f"{index}. {local}")

    escolha_local = int(input("\nEscolha um local (número): "))
    local_selecionado = list(atividades_pernambuco.keys())[escolha_local - 1]
    atividades = atividades_pernambuco[local_selecionado]

    print(f"\nAtividades disponíveis em {local_selecionado}:")
    for index, atividade in enumerate(atividades, start=1):
        print(f"{index}. {atividade['nome']}")

    escolha_atividade = int(input("Escolha uma atividade (número): "))
    atividade_selecionada = atividades[escolha_atividade - 1]

    # Exibindo detalhes da atividade selecionada
    print(f"\n--- {atividade_selecionada['nome']} ---")
    print(f"Descrição: {atividade_selecionada['descricao']}")
    print(f"Curiosidade: {atividade_selecionada['curiosidade']}")
    print(f"Dias disponíveis: {atividade_selecionada['dias']}")
    print(f"Horários: {atividade_selecionada['horarios']}")
    print(f"Valor: R$ {atividade_selecionada['valor']:.2f}")
    print(f"Restrições: {atividade_selecionada['restricao']}")
    exibir_imagem_atividade(atividade_selecionada['nome'])


# Função para exibir o dashboard personalizado
def exibir_dashboard():
    while True:
        print("--" * 20)
        print(f"\tOlá {usuario}, bem vindo a Nômade!\n No que podemos te ajudar?")
        print("--" * 20)
        print("1. Pesquisar Atividades Radicais")
        print("2. Planejar Roteiro")
        print("3. Ofertas e Descontos")
        print("4. Experiências Próximas")
        print("5. Acessar Perfil e Histórico")
        print("6. Buscar Hospedagem")
        print("--" * 20)
        escolha = input("Digite o número do que deseja fazer: ")
        print("--" * 20)

        if escolha == '1':
            pesquisar_atividades()
        elif escolha == '2':
            planejar_roteiro()
        elif escolha == '3':
            ofertas_descontos()
        elif escolha == '4':
            experiencias_proximas()
        elif escolha == '5':
            acessar_perfil()
        elif escolha == '6':
            buscar_hospedagem()
        else:
            print("Opção inválida!")
        print("--" * 20)
        if input("Deseja voltar ao menu principal? (s/n): ").lower() == 'n':
            break


# Função para planejar roteiro
def planejar_roteiro():
    print("\nPlanejar Roteiro")
    atividades_selecionadas = input("Digite os códigos das atividades selecionadas separados por vírgula: ").split(',')
    global rotas
    rotas = rotas.append({"usuario": usuario, "atividades": atividades_selecionadas}, ignore_index=True)
    print("Roteiro gerado com sucesso!")
    if input("Deseja compartilhar o roteiro com amigos por e-mail? (s/n): ").lower() == 's':
        email = input("Digite o e-mail do seu amigo: ")
        print(f"Roteiro enviado para {email} com sucesso!")


# Funções esboço para funcionalidades adicionais
def ofertas_descontos():
    print("Funcionalidade de Ofertas e Descontos ainda em desenvolvimento.")


def experiencias_proximas():
    print("Funcionalidade de Experiências Próximas ainda em desenvolvimento.")


def acessar_perfil():
    print("Funcionalidade de Perfil e Histórico ainda em desenvolvimento.")


def buscar_hospedagem():
    print("Funcionalidade de Hospedagem ainda em desenvolvimento.")


if __name__ == "__main__":
    print("Bem-vindo ao sistema Nômade Adventure!")

    # Verifica se o usuário deseja se registrar ou fazer login
    escolha_inicial = input("Você já possui uma conta? (s/n): ").strip().lower()
    if escolha_inicial == 'n':
        registrar_usuario()

    if fazer_login():
        exibir_dashboard()
        salvar_dados()  # Salva os dados no final da execução
    else:
        print("Não foi possível fazer login. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    print("Bem-vindo ao sistema Nômade Adventure!")
    if fazer_login():
        exibir_dashboard()
    else:
        print("Encerrando o programa. Verifique suas credenciais e tente novamente.")