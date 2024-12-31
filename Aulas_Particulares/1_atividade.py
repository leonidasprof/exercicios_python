Nome = input(f"digite o nome do funcionário:")
salario_bruto = float(input("Digite o salario do funcionário: "))
vale_refeicao = float(input("Digite o percentual do vale refeição:"))
vale_transporte = float(input("Digite o percentual do vale transporte:"))
valor_ref = salario_bruto * vale_refeicao
valor_trans = salario_bruto * vale_transporte
salario_liquido = salario_bruto - (valor_ref + valor_trans)
print(f" O salário líquido é: R${salario_liquido}")