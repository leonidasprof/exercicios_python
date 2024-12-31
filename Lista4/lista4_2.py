valores = []
listanova = list()
saida=[]

print("-"*40)
print(F"                LIMITANTES                    ")
print(f"-"*40)
limite_inferior = int(input(f"\nDigite valor para limite inferior:"))
limite_superior = int(input("Digite valor para limite superior:"))
print(f"-"*40)
for i in range(10):
    numero = (int(input(f"Digite o {i+1}º valor:")))
    valores.append(numero)
for num in valores:
    if num >= limite_inferior and num <= limite_superior:
        listanova.append(num)

listanova.sort()

print(f"-"*40)
print(f"O resultado é: {listanova}")
print(f"-"*40)

