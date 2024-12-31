def main():
    print(f"....Opções para Cadastramento.....")
    print(f"\n{categoria}\n")
    print(f"Obs.: no cadastro, você deve informar o número da opção corretamente.\n")


reptil = []
mamifero =[]
ave = []
outro = []
categoria =["1 - Réptil", "2 - Mamífero", "3 - ave", "4 - outro"]

main()

for i in range(10):
    animal = input(f"Cadastre o {i+1}º animal:")
    categ = int(input(f"Adcione a categoria assim como nas opções:"))

    if categ == 1:
        reptil.append(animal)
    elif categ == 2:
        mamifero.append(animal)
    elif categ == 3:
        ave.append(animal)
    else:
        outro.append(animal)

print(f"\n....Resultado do Cadastro....\n")
print(f"Répteis: {reptil} Quantidade: {len(reptil)}")
print(f"Mamíferos: {mamifero} Quantidade: {len(mamifero)}")
print(f"Aves: {ave} Quantidade: {len(ave)}")
print(f"Outros: {outro} Quantidade: {len(outro)}")






