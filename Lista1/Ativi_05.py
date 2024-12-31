time1 = input("Digite o nome do time1: ")
time2 = input("Digite o nome do time2: ")
gols1 = int(input("Digite total de gol do time 1: "))
gols2 = int(input("Digite total de gol do time 2: "))

if gols1> gols2:
    print(f"O ganhador foi o {time1} por {gols1}x{gols2}")
elif gols2> gols1:
    print(f"O ganhador foi o {time2} por {gols2}x{gols1}")
else:
    print(f"Resultado: {time1} empatou com o {time2} em {gols1} x {gols2}")
