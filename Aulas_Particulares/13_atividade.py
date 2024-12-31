base_inferior = 1100
base_media = 2000
base_inf = 0.10
base_med = 0.07
base_sup = 0.05
sal_bruto = 0.0
salario_liquido = 0.0
print(0.10*sal_bruto)
cont = 0

while True:

    sal_bruto = float(input(f"Digite o {cont+1}º Salário bruto ou (0.0) para finalizar: "))
    if sal_bruto == 0.0:
        break
    elif sal_bruto < base_inferior:
        salario_liquido = (base_inf * sal_bruto) + sal_bruto
    elif sal_bruto <= base_media:
        salario_liquido = (base_med * sal_bruto) + sal_bruto
    else:
        salario_liquido = (base_sup * sal_bruto) + sal_bruto

    print(f"Seu novo salário é: R${salario_liquido}")

    cont += 1



