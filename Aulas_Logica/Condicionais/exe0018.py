soma_notas = 0
contador_notas = 0

while True:
    nota = float(input("Digite a nota do aluno (-1 para encerrar): "))

    if nota == -1:
        break

    soma_notas += nota
    contador_notas += 1

if contador_notas == 0:
    print("Nenhuma nota foi informada. ")
else:
    media = soma_notas / contador_notas
    print(f"Foram informadas {contador_notas} notas. ")
    print(f"A média das notas é: {media:.2f} ")
