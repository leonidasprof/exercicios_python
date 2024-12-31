cont = 0
maior_idade = -1
menor_idade = 999999

while True:
    idade = int(input(f'Digite a {cont+1}ª idade: '))
    if idade == 100:
        break
    if idade > maior_idade:
        maior_idade = idade
    cont +=1

printf(f"A maior idade é: {maior_idade}\n ")

