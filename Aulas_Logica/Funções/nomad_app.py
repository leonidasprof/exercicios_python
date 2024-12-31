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
    print(f"Link para imagem: {url_imagem}\n")

# Função para pesquisar atividades radicais por localização em Pernambuco
def pesquisar_atividades():
    print("--"*30)
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

    # Exibição de imagem relacionada ao passeio
    exibir_imagem_atividade(atividade_selecionada['nome'])

# Função para exibir o dashboard personalizado
def exibir_dashboard():
    while True:
        print("--"*20)
        print(f"\tOlá,seja bem vindo a Nômade Adventure!\n No que podemos te ajudar?")
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
        print("--"*20)
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

    # Obtendo clima usando API OpenWeather
    api_key = "SUA_API_KEY_AQUI"
    clima_url = f"http://api.openweathermap.org/data/2.5/weather?q={localizacao}&appid={api_key}"
    try:
        response = requests.get(clima_url)
        response.raise_for_status()
        clima_data = response.json()
        clima = clima_data['weather'][0]['description']
        print(f"Clima em {localizacao}: {clima}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o clima: {e}")
        clima = "desconhecido"

    # Filtros de pesquisa
    filtro = (atividades['localizacao'] == localizacao) & (atividades['dificuldade'] == dificuldade) & (
                atividades['clima'] == clima)
    resultados = atividades[filtro]

    if resultados.empty:
        print("Nenhuma atividade encontrada com esses filtros.")
    else:
        print(resultados)
        if input("Deseja reservar alguma atividade? (s/n): ").lower() == 's':
            codigo_atividade = input("Digite o código da atividade para reservar: ")
            print(f"Atividade {codigo_atividade} reservada com sucesso!")


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
        response.raise_for_status()
        hospedagens = response.json()
        print("Opções de hospedagem:")
        for hospedagem in hospedagens:
            print(f"{hospedagem['nome']} - Preço: {hospedagem['preco']}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar hospedagens: {e}")

# Função principal
def main():
    print("--" * 20)
    print("\tBem-vindo ao Nômade Adventure!")
    print("--" * 20)

    while True:
        if input(f"\nJá tem cadastro? (s/n): ").lower() == 's':
            if fazer_login():
                exibir_dashboard()
                break
            else:
                print("Erro no login. Tente novamente.")
                if input("Deseja tentar novamente? (s/n): ").lower() != 's':
                    print("Encerrando o sistema. Até mais, aventureiro!")
                    return
        else:
            registrar_usuario()
            exibir_dashboard()
            break

    print("Até mais, aventureiro!")

if __name__ == "__main__":
    main()