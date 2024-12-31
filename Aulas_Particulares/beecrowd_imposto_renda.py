
salario = float(input())

while True:
    if salario <= 2000.00:
        desconto = "Isento"
        print(desconto)
        break
    elif salario <= 3000.00:
        desconto = (8 / 100) * (salario - 2000.00)
        print(f"R$ {desconto:.2f}")
        break
    elif salario <= 4500.00:
        desconto = (8 / 100) * 1000.00 + (18 / 100) * (salario - 3000.00)
        print(f"R$ {desconto:.2f}")
        break
    elif salario > 4500.00:
        desconto = (8 / 100) * 1000.00 + (18 / 100) * 1500.00 + (28 / 100) * (salario - 4500.00)
        print(f"R$ {desconto:.2f}")
        break

