aluno = input("Digite o nome do aluno: ")
per_falta = float(input("Digite o percentual de faltas: "))
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
media = (nota1+nota2)/2

if per_falta>=75:
    print(f"\n{aluno}, você foi reprovado. Sua média foi: {media}")
elif media<7:
    print(f"\n{aluno}, você foireprovado. Sua média foi: {media} ")
else:
    print(f"\n{aluno}, você aprovado, sua média foi: {media} ")

