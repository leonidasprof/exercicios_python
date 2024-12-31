print("--"*18)
print("              >TREINA RECIFE             ")
print("           .FOLHA DE PAGAMENTO.            ")
print("--"*18)

nome_prf = input(f"Digite o nome do professor: ").upper()
qt_horas = int(input(f"Digite a quantdade de horas dadas no mês: \n "))
valor_hora = float(input(f"Digite o valor da hora: \n "))

print("--" * 18)
print(f"O salário de {nome_prf} no mês foi:\n -------> {(qt_horas * valor_hora):.2f} ")
print("--" * 18)
