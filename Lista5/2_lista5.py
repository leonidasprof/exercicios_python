nome_arquivo = "./arquivo_lista5.txt"
print("\n          VERIFICAÇÃO         ")

with open(nome_arquivo, "r", encoding="UTF-8") as file:
    ips = file.readlines()

for ip in ips:
    ip = ip.strip()
    partes_ip =ip.split(".")

    if len(partes_ip) == 4:
        situacao = ""

        for parte in partes_ip:
            if int(parte) < 0 or int(parte) > 255:
                situacao = "inválido"
                break
            else:
                situacao = "válido"


                print("-" * 30)
                print(f"ip ({ip}) está {situacao}!")










