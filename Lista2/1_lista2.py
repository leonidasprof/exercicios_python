qt_pessoas = 0
media_peso = 0
acima_peso = 0
kg = 0

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º paciente: ")
    peso = float(input(f"Digite o peso do {i+1}º paciente: "))

    if nome != 0:
        qt_pessoas += i
        kg += peso
    if peso > 80:
       acima_peso += i


media_peso = kg / qt_pessoas

print(f"\nA média de peso é: {media_peso:.2f}Kg")
print(f"A quantidade de pessoas acima do peso é: {acima_peso}")
