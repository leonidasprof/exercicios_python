def new_func():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"]
    nome1 = [nome for nome in nomes if len(nome) > 5]
    print(nome1)

new_func()
