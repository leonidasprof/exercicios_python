num_tabuada = int(input(f"Digite o número da tabuada: "))
inicio = int(input(f"Digite o número que você deseja iniciar: "))
fim = int(input(f"Digite o número que você deseje que finalize: "))
calc = 0

for i in range(inicio-1,fim):
    calc = i + 1
    print(f"{num_tabuada}*{i+1} = {num_tabuada*calc} ")