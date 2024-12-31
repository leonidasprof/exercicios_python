cont = 0
print("--"*18)
print("              TREINA RECIFE             ")
print("          LÓGICA DE PROGRAMAÇÃO            ")
print("           Pof. Rogério Aguiar             ")
print("--"*18)

while True:
    nome = input(f"Digite o nome do aluno OU\n(Digite PARAR para finalizar) ").upper()
    nota1 = float(input(f"Digite a {cont+1}ª nota: \n "))
    nota2 = float(input(f"Digite a {cont+2}ª nota: \n "))
    print("--" * 18)
    print(f"A média do aluno é:\n -------> {((nota1 + nota2) / 2):.2f} ")
    print("--" * 18)
print("--"*18)


