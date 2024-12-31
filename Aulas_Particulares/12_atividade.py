peixes = []
cont = 0
soma_peixes = 0
multa = 0.0

while True:
    peixes1 = float(input(f"Digite o peso do {cont+1}º peixe: (digite -1 para sair)\n ----> "))
    if peixes1 == -1:
        break
    else:
        peixes.append(peixes1)
        soma_peixes = sum(peixes)

if soma_peixes > 50:
    multa = 4 * soma_peixes

soma_peixes += 1

print(f"Foram pescados {soma_peixes}kg de peixes.")
print(f"A multa por kg de peixes é: R${multa}")
