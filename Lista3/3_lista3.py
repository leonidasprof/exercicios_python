numeros = []
negativos = 0
positivos = 0

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

for elementos in numeros:
    if elementos < 0:
        negativos += 1

    elif elementos > 0:
        positivos += elementos

print(f"\n-----------RESPOSTAS-----------\n")
print(f"A quantidade de números negativos é: {negativos}")
print(f"A soma dos números positivos é: {positivos}")



