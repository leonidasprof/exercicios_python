print("--"*18)
print("              RATEIO              ")
print("--"*18)

valor_apartamento = int(input("Qual a quantidade de apartamentos?\n "))
valor_agua = float(input("Qual o valor da cota de água?\n "))
valor_energia = float(input("Qual o valor da cota de energia?\n "))
rateio = float(valor_agua + valor_energia) / valor_apartamento

print("--"*18)
print(f"O rateio por apartamento ficou:\n ------->  R${rateio:.2f} ")
print("--"*18)