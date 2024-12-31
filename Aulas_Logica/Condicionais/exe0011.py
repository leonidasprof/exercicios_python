cod_user = 1234
senha_user = 9999
cod = int(input("Digite o código do usuário: "))

if cod != cod_user:
    print("Código inválido")

else:
    senha = int(input("Digite sua senha: "))
    if senha != senha_user:
        print("senha inválida")
    else:
        print("Login Identificado")

