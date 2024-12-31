def soma(n1, n2):
    return n1+n2

def subtracao(n1, n2):
    return n1-n2

def multiplicacao(n1, n2):
    return n1*n2

def divisao (n1, n2):
    if n1>=n2:
        return n1/n2
    else:
        return n2/n1

print(f"\n------------------------CALCULADORA------------------------\n")
continuar = input(f"Deseja realizar uma operação? [S] ou [N]: ").upper()

while continuar == "S":

    num1 = int(input(f"Digite o primeiro valor: "))
    num2 = int(input(f"Digite o segundo valor: "))
    print("\n[S] soma [B] Subitração [M] Multiplição [D] Divisão")
    opcao = input(f"Digite qual opção você deseja: ").upper()
    print(f"A resposta da operação é:")

    if opcao == "S":
        print(soma(num1, num2))
    elif opcao == "B":
        print(subtracao(num1, num2))
    elif opcao == "M":
        print(multiplicacao(num1, num2))
    else:
        print(divisao(num1, num2))

    continuar = input(f"\nDeseja continuar operação? [S] ou [N]: ").upper()
    if continuar == "N":
        print(f"\nObrigado pela experiência!")


