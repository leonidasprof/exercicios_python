print("--"*20)
print("            PROVA DE FUNDAMENTOS")
print("                   CESAR")
print("--"*20)
codigos = ["61", "71", "11", "21", "32", "19", "27", "31"]
cidades = ["Brasilia", "Salvador", "São Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]
cont = 0
ddds = []

for i in range(5):
    ddd = int(input(f"Digite a {i+1}º DDD: "))
    ddds.append(ddd)
print("--"*30)
print("                   DDDs PESQUISADOS ")
print("--"*30)
for num in ddds:
    if num == 61:
        print(f"O DDD {codigos[0]} pertence a: {cidades[0]}.")
    elif num == 71:
        print(f"O DDD {codigos[1]} pertence a: {cidades[1]}.")
    elif num == 11:
        print(f"O DDD {codigos[2]} pertence a: {cidades[2]}.")
    elif num == 21:
        print(f"O DDD {codigos[3]} pertence a: {cidades[3]}.")
    elif num == 32:
        print(f"O DDD {codigos[4]} pertence a: {cidades[4]}.")
    elif num == 19:
        print(f"O DDD {codigos[5]} pertence a: {cidades[5]}.")
    elif num == 27:
        print(f"O DDD {codigos[6]} pertence a: {cidades[6]}.")
    elif num == 31:
        print(f"O DDD {codigos[7]} pertence a: {cidades[7]}.")
    else:
        print(f"Esse DDD não foi cadastrado.")

    cont += 1

print("--"*30)
