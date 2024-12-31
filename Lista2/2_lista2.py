def main():
    print(f"\nFUNERÁRIA SUA HORA CHEGOU!\n ")


cont = 1
qt_codigo = 0

main()

while True:
    codigo = int(input(f"Cadastre o código do {qt_codigo+1}º caixão ou -1 para finalizar cadastro: "))

    if codigo == -1:
        break

    qt_codigo += 1

if qt_codigo == 0:
    print(f"Nenhum cadastro foi realizado.")

else:
    print(f"A quantidade de caixões cadastrados foi: {qt_codigo}")
