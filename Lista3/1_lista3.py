def main():
    print("__"*30)
    print("          ***********    PESQUISA   *************")
    print("__" * 30)
    print(f"\nQual o melhor Sistema Operacional, para operar em Servidores?\n")
    for indice, elemento in enumerate(sistemas):
        print(f"{indice}:{elemento}\t")
    print("__" * 30)
    print("Digite (sair) para finalisar.")


votos = []
sistemas = ["Windows Server", "Mac OS", "Linux", "Outro"]
contador = 0
voto = True

main()

while voto != "sair":
    voto = input(f"\nQual O.S. você prefere? ")
    if voto == "sair":
        break

    contador += 1

    for num in voto:
        votos.append(num)
print("__"*30)
print(f"\n********************    RESULTADO    ***********************")
print("__"*30)
print(f"\nVotos em {sistemas[0]}: {votos.count('0')}")
print(f"{(votos.count("0")/contador*100)}% preferem {sistemas[0]}.")
print(f"Votos em {sistemas[1]}: {votos.count('1')}")
print(f"{(votos.count("1")/contador*100)}% preferem {sistemas[1]}.")
print(f"Votos em {sistemas[2]}: {votos.count('2')}")
print(f"{(votos.count("2")/contador*100)}% preferem {sistemas[2]}.")
print(f"Votos em {sistemas[3]}: {votos.count('3')}")
print(f"{(votos.count("3")/contador*100)}% preferem {sistemas[3]} opção.")
print("__"*30)