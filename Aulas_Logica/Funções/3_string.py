frase = input("Digite uma frase:")
palavra = input("Digite uma palavra contida na frase: ")
nova_palavra = input("Digite a palavra pela qual você deseja substituir: ")

frase_modificada = frase.replace(palavra, nova_palavra).upper()

print(frase_modificada)
