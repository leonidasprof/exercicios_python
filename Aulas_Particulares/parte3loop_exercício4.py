#Maior e Menor de Três números
maior = -1
menor = 9999999
for qtd_bolas in range (3):
    n = int(input("O número da bola: "))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f"Maior: {maior}, Menor: {menor}")