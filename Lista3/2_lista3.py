numeros = []
contador = 0
numero_in = True


while numero_in != "-1":
    numero_in = input(f"\nDigite um número inteiro? ")
    if numero_in == "-1":
        break

    contador += 1

    for num in numero_in:
        numeros.append(num)
        lista_ordenada = sorted(numeros, reverse=True)

print(f"\n_______________________      RESPOSTAS     ____________________________\n")
print(f"A quantidade de números digitados foi: {len(numeros)}.")
print(f"A ordem decrescente dos números é: {lista_ordenada}")
print(f"Quantas vezes o valor '5' aparece na lista? {numeros.count("5")} vezes.")