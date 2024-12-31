altura = 0
sexo = ""
menoraltura = 999999
media_altura = 0
soma_altura = 0
contm = 0

for i in range (5):
    sexo = input(f"Digite M ou F para indicar o sexo: ").upper()
    altura = float(input(f"Digite a altura:"))
    if sexo == "M":
        soma_altura = soma_altura + altura
        if altura < menoraltura:
            menoraltura = altura
        contm += 1

media_altura = soma_altura / contm
print(f"Menor altura: {menoraltura}, Media da altura dos meninos: {media_altura:.3}m")


