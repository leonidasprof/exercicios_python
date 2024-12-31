sub = 0
mult = 0
div = 0
Adi = 0
calculo = ["    1 - adção", "2 - Subtração", "3 - Multiplicação", "4 - Divisão" ]
largura_total = 30
texto = "".join(map(str, calculo))

print("--"*32)
print("                         TREINA RECIFE             ")
print("                          CALCULADORA         ")
print("--"*32)
print("                             MENU             ")
print("--"*32)
print(*calculo)
print("--"*32)
numero = float(input(f"\tDigite o 1º número: "))
numero1 = float(input(f"\tDigite o 2º número: "))
numero2 = int(input(f"\tDigite uma opção de cálculo: "))
print("--" * 32)
if numero2 == 1:
    adi = numero + numero1
    print(f"\tO resultado é:  ------> {adi} ")
elif numero2 == 2:
    sub = numero - numero1
    print(f"\tO resultado é:  ------> {sub} ")
elif numero2 == 3:
    mult = numero * numero1
    print(f"\tO resultado é:  ------> {mult} ")
else:
    div = numero / numero1
    print(f"\tO resultado é:  ------> {div} ")
print("--" * 32)
