calculos = []
quadrado = []

for i in range(10):
    numero = float(input(f"Digite {i+1}º número real: "))
    calculos.append(numero)

for numeros in calculos:
    numeros = numeros**2
    quadrado.append(numeros)

print(f"\n...............RESPOSTAS...................\n")
print(f"Os numeros digitados foram: {calculos}")
print(f"O quadrado de cada número real digitado foi: {quadrado}")
