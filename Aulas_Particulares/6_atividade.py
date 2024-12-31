print("--"*18)
print("           TREINA RECIFE             ")
print("         ATIVIDADE PRÁTICA            ")
print("--"*18)

carro = input(f"digite o modelo d carro: ")
litros_km = float(input("Quantos km ele faz com 1l?: "))
km_percorrido = int(input(f"Quantos km você irá percorrer? "))
valor_combustiel = float(input("Digite o valor do litro de combustível: "))

km_litros = km_percorrido / litros_km

print("--" * 18)
print(f"O carro de modelo {carro} ao percorrer\n{km_percorrido}Km gastará: {km_litros:.2f} litros  ")
print(f"O gasto com combustível será: R${km_litros*valor_combustiel:.2f}\n  ")
print("--" * 18)