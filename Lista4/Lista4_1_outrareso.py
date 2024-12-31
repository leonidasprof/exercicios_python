dia = str(input("Digite o dia do seu aniversario: "))
mes = str(input("Digite o mes do seu aniversario: "))
ano = str(input("Digite o ano do seu aniversario: "))

print(f"sua senha é: {mes}${dia[::-1]}#{dia}!{mes[::-1]}*{ano} ")
