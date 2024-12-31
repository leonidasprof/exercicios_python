print("--"*18)
print("           CALCULO IDADES")
print(f"--"*18)

soma_idades = 0
maior_idade = 0
menor_idade = 0
media_idades = 0
qt_idades = 0
idades = list()

for i in range(6):
    idade = int(input(f"Digite a {i+1}ª idade: "))
    idades.append(idade)

    soma_idades = sum(idades)
    maior_idade = max(idades)
    menor_idade = min(idades)
    qt_idades = len(idades)

media_idades = soma_idades / qt_idades
print(f"--"*18)
print(f"             RESULTADOS")
print(f"--"*18)
print(f"O total de idades lidas foram: {qt_idades} ")
print(f"A maior idade é: {maior_idade} ")
print(f"A menor idade é: {menor_idade} ")
print(f"A média de idades é: {media_idades:.0f} anos ")
print(f"--"*18)


