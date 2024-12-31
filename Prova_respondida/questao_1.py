print("--"*20)
print("            PROVA DE FUNDAMENTOS")
print("                   CESAR")
print("--"*20)
alturas = []
abaixo = 0
pertence = ()
cont = 0

for i in range(5):
    altura = float(input(f"Digite a {i+1}ª altura: "))
    alturas.append(altura)
print("--"*30)
for num in alturas:
    if num < 1.50:
        abaixo += 1
    if num == 1.80:
        pertence = "A altura 1.80 faz parte da lista."
    else:
        pertence = "A altura 1.80 não faz parte da lista. "


        cont += 1

alturas.sort()
print("                        RESULTADOS ")
print("--"*30)
print(f"A ordem crescente é: {alturas} ")
print(pertence)
print(f"A quantidade de alturas abaixo de 1.50 foi: {abaixo}")
print("--"*30)

