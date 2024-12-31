import os



salario = float(input())

while True:
    if salario <= 2000.00:
        desconto = "Isento"
        print(desconto)
        break
    if salario <= 3000.00:
        desconto = (8 / 100) * salario 
        print(f"R$ {desconto:.2f}")
        break
    if salario <= 4500.00:
        desconto = (18 /100) * salario
        print(f"R$ {desconto:.2f}")
        break
    if desconto > 4500.00:
        desconto = (28 / 100) * salario
        print(f"R$ {desconto:.2f}")
        break

print("Valor inválido, digite um salário válido.")



