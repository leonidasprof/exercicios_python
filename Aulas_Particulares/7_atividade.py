print("--"*18)
print("              TREINA RECIFE             ")
print("           FOLHA DE PAGAMENTO            ")
print("--"*18)

nome = input(f"digite o nome do funcionário:")
salario_fixo = float(input("Digite o salario fixo: "))
comissao = salario_bruto * 0.15

print("--" * 18)
print(f"A comissão de {nome} foi ------>{comissao}")
print(f"O salário de {nome} no mês foi:\n -------> R${(salario_fixo * comissao):.2f} ")
print("--" * 18)