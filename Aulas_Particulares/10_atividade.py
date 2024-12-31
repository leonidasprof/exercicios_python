adicional = 50.00

print("--"*18)
print("              TREINA RECIFE             ")
print("                Show Life           ")
print("--"*18)

valor_hora = float(input(f"Qual o valor da hora (SHOW): "))
distancia = float(input(f"Qual a distância? (km): "))
duracao_show = float(input(f"Qual a duração do Show? (Hora): "))
frete = distancia * 0.35
print("--" * 18)
print(f"O valor do show é:  ------>R${(valor_hora*duracao_show)+adicional} ")
print(f"O valor do frete é:  ------>R${frete}")
print("--" * 18)