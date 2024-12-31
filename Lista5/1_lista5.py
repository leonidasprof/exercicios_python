numeros = []
maiores = menores = 0

for i in range(10):
    valor = int(input(f"Insira o {i+1}º valor: "))
    numeros.append(valor)

    if i > 0:
        if valor > numeros[0]:
            maiores += 1
        elif valor < numeros[0]:
            menores += 1

print(f"O primeiro valor da lista é {numeros[0]} e ele se repete {numeros.count(numeros[0])} vezes.")
print(f"Existem {maiores} número(s) maiores que o primeiro da lista")
print(f"Existem {menores} número(s) menores que o primeiro da lista")
