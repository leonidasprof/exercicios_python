valor_desconto = 0
percent4 = 0.4
percent3 = 0.3
percent2 = 0.2
percent1 = 0.1
percent = ()

for i in range(2):
    codigo = int(input(f"\nDigite o código do {i+1}º produto: "))
    valor_unit = float(input(f"Digite o valor unitário do {i+1}º produto: "))
    total_estoque = int(input(f"Digite a quantidade do {i+1}º produto em estoque: "))

    if valor_unit >= 0 and valor_unit <= 2:
        valor_desconto = valor_unit - (valor_unit*percent4)
        percent = str("40%")
    elif valor_unit >= 3 and valor_unit <= 5:
        valor_desconto = valor_unit - (valor_unit*percent3)
        percent = str("30%")
    elif valor_unit >= 6 and valor_unit <= 9:
        valor_desconto = valor_unit - (valor_unit*percent2)
        percent = str("20%")
    else:
        valor_desconto = valor_unit - (valor_unit*percent1)
        percent = str("10%")

        print(f"\nO valor unitário do {i+1}º produto é:R$ {valor_unit}" )
        print(f"O desconto aplicado foi de: {percent}")
        print(f"O valor com desconto é: R$ {valor_desconto:.2f}" )

