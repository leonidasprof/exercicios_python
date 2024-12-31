primeira_parte =()
segunda_parte = ()
senha = ()
nome = input("Digite um nome com no mínimo 10 caracteres:")
primeira_parte = nome[:6]
segunda_parte = nome[6:]
senha = segunda_parte[:2] + "%%" + primeira_parte[3:]
print(senha)
print(segunda_parte)