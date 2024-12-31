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
    # Adicione mais locais e atividades conforme necessário
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
    preferencias = input("Digite suas preferências: ")
    global usuarios
    usuarios = usuarios.append({"usuario": usuario, "senha": senha, "preferencias": preferencias}, ignore_index=True)
    print("Usuário registrado com sucesso!")

# Função para fazer login
def fazer_login():
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
    # Exemplo de link de imagem para demonstração
    url_imagem = f"https://exemplo.com/imagens/{nome_atividade.replace(' ', '_').lower()}.jpg"
    print(f"Link para imagem: {url_imagem}")

# Função para pesquisar atividades radicais por localização em Pernambuco
def pesquisar_atividades():
    print("\nLocais disponíveis para atividades radicais em Pernambuco:")
    for index, local in enumerate(atividades_pernambuco.keys(), start=1):
        print(f"{index}. {local}")

    escolha_local = int(input("Escolha um local (número): "))
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

    # Exibição de imagem relacionada ao passeio
    exibir_imagem_atividade(atividade_selecionada['nome'])

# Função para exibir o dashboard personalizado
def exibir_dashboard():
    while True:
        print("\nDashboard")
        print("1. Pesquisar Atividades Radicais")
        print("2. Planejar Roteiro")
        print("3. Ofertas e Descontos")
        print("4. Experiências Próximas")
        print("5. Acessar Perfil e Histórico")
        print("6. Buscar Hospedagem")
        escolha = input("Escolha uma opção: ")

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
        if input("Deseja sair do Dashboard? (s/n): ").lower() == 's':
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

# Função para exibir ofertas e descontos
def ofertas_descontos():
    print("\nOfertas e Descontos")
    # Exemplo de simulação de ofertas
    print("1. Desconto de 20% em escalada")
    print("2. Desconto de 15% em rapel")
    if input("Deseja ativar alerta de preço? (s/n): ").lower() == 's':
        print("Alerta de preço ativado!")

# Função para exibir experiências próximas
def experiencias_proximas():
    print("\nExperiências Próximas")
    print("1. Grupo de escalada")
    print("2. Grupo de rapel")
    if input("Deseja participar de algum grupo? (s/n): ").lower() == 's':
        print("Participação confirmada no grupo!")

# Função para acessar perfil e histórico
def acessar_perfil():
    print("\nPerfil e Histórico")
    print("1. Avaliar atividade")
    print("2. Ver ranking de aventura")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        print("Avaliação registrada com sucesso!")
    elif escolha == '2':
        print("Ranking de aventura exibido!")
    else:
        print("Opção inválida!")

# Função para buscar hospedagem usando uma API fictícia
def buscar_hospedagem():
    print("\nBuscar Hospedagem")
    localizacao = input("Digite a localização: ")
    # Simulando uma resposta fictícia
    try:
        response = requests.get(f"http://ficticia.api/hospedagem?local={localizacao}")
