pecas_compradas = int(input("Digite a quantidade de peças: "))
valor_total = float(input("\nDigite o valor total da compra: "))
codigo = int(input(f"""Qual foi a forma de pagamento?
      1. À vista
      2. Crédito
      3. Crédito Parcelado\n
      Digite o código referente a compra:"""))

if pecas_compradas>2 and codigo==1:
    valorcom_desconto = valor_total - (valor_total*0.20)
    print(f"Descconto Aprovado!\nO valor a pagar é: R$", valorcom_desconto)
else:
    print("Infelizmente você não possue desconto!")