i = 0
menorpeso = 0
maiorpeso = 0

while True:
    peso = float(input(f"Digite o {i + 1}º peso:"))
    if peso > 200:
        break
    if menorpeso == 0 or peso < menorpeso:
        menorpeso = peso
    if maiorpeso == 0 or peso > maiorpeso:
        maiorpeso = peso
    i +=1

print(f"\t Quantidade de pesos: {i}\n\t Menor peso é: {menorpeso}\n\t Maior peso é: {maiorpeso}")

