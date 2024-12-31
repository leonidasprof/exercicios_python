cont = 0
maior_frase= -1

for qtd in range(50):
    frase = input(f'Digite a {cont+1}ª frase: ')
    tam_frase = len(frase)
    if tam_frase > maior_frase:
        maior_frase = tam_frase
        conlusao = frase

    cont +=1

printf(f"A maior frase é: {conlusao} e tem {maior_frase} posições\n ")