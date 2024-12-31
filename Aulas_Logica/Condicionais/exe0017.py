nota = 0.0
i = 0
soma_notas = 0.0

while nota != -1:
    nota = float(input("Digite uma nota ou -1 para finalizar: "))

    if nota != -1:
        i = i + 1
        soma_notas = soma_notas + nota

media = soma_notas / i
print(f"Quantidade de notas informadas: {i}")
print(f"Média das notas: {media}")
