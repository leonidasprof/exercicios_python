import os
os.system("cls")
from datetime import date

ano_atual = date.today().year
ano_demissao = int(input("Digite o ano da sua admissão: "))
salario_atual = float(input("Digite seu salário atual: "))
ano_reajuste = int(input("Digite o último ano do reajuste salarial: "))

tempo_aumento = ano_atual - ano_reajuste
anos_trabalhados = ano_atual - ano_demissao

if tempo_aumento>=2:
    if anos_trabalhados>10:
        novo_salario = salario_atual*1.30
    elif anos_trabalhados>=5 and anos_trabalhados<=10:
        novo_salario = salario_atual*1.20
    else:
        novo_salario = salario_atual*1.10
    print("\nApto a receber reajste salarial! ")
    print("Novo salário R$", novo_salario)
else:
    print("\nNão está apto a receber reajuste salarial! ")


