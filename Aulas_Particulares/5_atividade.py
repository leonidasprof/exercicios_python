print("--"*18)
print("              TREINA RECIFE             ")
print("           FOLHA DE PAGAMENTO            ")
print("--"*18)

nome = input(f"digite o nome do funcionário:")
salario_bruto = float(input("Digite o salario do funcionário: "))
valor_ir = salario_bruto * 0.05
valor_inss = salario_bruto * 0.11
descontos = valor_ir + valor_inss

print("--" * 18)
print(f"O desconto do IR foi ------>{valor_ir}")
print(f"O desconto do INSS foi ------>{valor_inss}")
print(f"O salário líquido de {nome} no mês foi:\n -------> R${(salario_bruto - descontos):.2f} ")
print("--" * 18)