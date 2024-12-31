'''n1 = int(input())
n2 = int(input())
print(n1 + n2)'''

'''numeros = [1, 2, 3, 4, 5]
dobrados = [n * 2 for n in numeros]
print(dobrados)'''

'''numeros = [1, 2, 3, 4, 5]
impares = [n for n in numeros if n % 2 != 0]
print(impares)'''

'''print("Primeira linha", end=" | ")
print("Segunda linha")
# Saída: Primeira linha | Segunda linha'''

'''print('Python', 'é', 'fantástico', sep='-')
# Saída: Python-é-fantástico'''

'''nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"]
primeiro, *segundo, ultimo = nomes
print(primeiro)
print(segundo)
print(ultimo)'''

'''
print([i**2 for i in range(1,11)])'''

nome1 = []
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"]
nome1 = [nome for nome in nomes if len(nome) > 5]
print(nome1)


