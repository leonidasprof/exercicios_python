ir0 = 0
ir1 = 0.10
ir2 = 0.15
ir3 = 0.25
ali1 = 900.0
ali2 = 1500.0
ali3 = 2500.0
casal = list()

casal1 = str(input(f"Digite o nome do casal: EX.:(nome1 e nome2)\n ---> "))
rh = float(input(f"Digite a renda do homem: "))
rm = float(input(f"digite a renda da mulher: "))
renda = rh + rm

if renda <= 900:
    ir = (renda * ir)
elif renda > ali1 and renda <= ali2:
    ir = (renda * ir1)
elif renda > ali2 and renda <= ali3:
    ir = (renda * ir2)
else:
    ir = (renda * ir3)

print(f"A renda de {casal1} é: R${renda}")
print(f"O valor da alíquota é:")
if renda <900:
    print(f"{ir0}%")
if renda <= 1500:
    print(f"{ir1}%")
if renda <= 2500:
    print(f"{ir2}%")
else:
    print(f"{ir3}%")
print(f"o Valor a pagar é: R${ir}")
print(f"A renda líquda é: R${renda-ir}")
