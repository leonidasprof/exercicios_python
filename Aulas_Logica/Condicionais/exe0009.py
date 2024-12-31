nome = input("nome do aluno: ")
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

media = (nota1*2) + (nota2*3) + (nota3*5) / 10

if media<5:
    print("Situação: Reprovado ")

elif media>=5 or media<=6.9:
    print("Situação: Recuperação ")

else:
    print("Situação: Aprovado")