qt_let = 0
inver = ()

frase1 = input("Digite uma frase:").upper()
inver = frase1[::-1]
qt_let = frase1.count("A")
print(f"Qt de letras da frase é: {qt_let} ")
print(f"A frase invertida fica: {inver} ")

