carros: int = int(input("Digite a quantidade de carros vendidos: "))
venda = float(input("Digite o valor total de vendas: "))
salario_fixo = float(input("Digite o salário fixo mensal: "))
comissao = float(input("Digite o valor da comissão por carro vendido: "))

salario_final = salario_fixo + (comissao*carros) + (venda*0.05)

print(f"Salário do vendedor é: R$ {salario_final:.2f} ")

