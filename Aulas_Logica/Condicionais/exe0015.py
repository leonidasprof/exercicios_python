
n = int(input("Digite o tam da seq: "))
cont = conta_par = conta_impar = 0
soma_par = 0
soma_impar = 0
soma = 0
soma1 = 0

while cont < n:
    num = int(input("Digite um num da seq: "))
    cont = cont + 1
    if num % 2 == 0:
        conta_par = conta_par + 1
        soma_par += num


    else:
        conta_impar += 1
        soma_impar += num

print(f"A soma dos números pares é: {soma_par} ")
print(conta_par,   "numeros pares:")
print(f"A soma dos números impares é: {soma_impar} ")
print(conta_impar, "numeros impares:")

