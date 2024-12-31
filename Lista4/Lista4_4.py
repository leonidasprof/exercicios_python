import os
os.system('cls')

def minutos(x):
    return x*60
def segundos(x):
    return x*360
def converter(opcao, x):
    if opcao not in (1,2):
        print('Opção inválida! Escolha entre 1 ou 2.')
        return
    elif opcao == 1:
        novo_valor = minutos(horas) # horas*60
    else:
        novo_valor = segundos(horas) #horas*360
    return novo_valor

print("__"*14)
print("            CONVERSOR" )
print("__"*15)
horas = float(input('Informe o valor em horas:'))
print("__"*15)
print('\t         MENU')
print("__"*15)
option = int(input('Você deseja converter para:\n1 - MINUTOS\n2 - SEGUNDOS\n_________________->'))

print(converter(option, horas))
print("__"*15)
