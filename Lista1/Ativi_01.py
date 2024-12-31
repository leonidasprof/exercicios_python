hora_mes = float(input("Digite a quantidade de atividades? (horas) realizadas esse mês: "))

if hora_mes <= 10:
    qt_pontos = hora_mes * 2
    print("Seu número de pontos é:", qt_pontos)
    if hora_mes >= 11 and hora_mes <= 20:
        qt_pontos = hora_mes*5
        print(f"Seu número de pontos é: {qt_pontos})
else:
    qt_pontos = hora_mes * 10
    print(f"Seu número de pontos é: {qt_pontos} ")