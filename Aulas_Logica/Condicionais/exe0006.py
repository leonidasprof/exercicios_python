valor_compra = float(input("Digite o valor da compra: "))
cupom = input("Digite o nome do cupom de descontos: ")

if cupom == "CESAR" or cupom == "CESARSCH":
    valor_total = valor_compra - (valor_compra*0.15)

print(f"\no Valor a pagar é: {valor_total:.2f} ")