print("--"*18)
print("              TREINA RECIFE             ")
print("                 ENERGIA           ")
print("--"*18)

salario_minimo = float(input(f"Digite o valor do salário mínimo: "))
consumo_quilowats = int(input(f"Qual o consumo (quilowats) da residência: "))
valor_quilowats = salario_minimo / 1000
print("--" * 18)
print(f"O valor do quilowats é:  ------>R${valor_quilowats} ")
print(f"O valor da conta é:  ------>R${consumo_quilowats*valor_quilowats}")
print(f"O valor da conta com desconto:-------> R${(consumo_quilowats * valor_quilowats)*0.15} ")
print("--" * 18)