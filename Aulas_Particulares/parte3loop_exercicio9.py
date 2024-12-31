perda_massa = 50
massa = float(input(f"Digite a massa do material: "))
massa_final = massa
tempo = 0
cont = 0

while massa_final > 0.5:
    massa_final = massa_final / 2
    tempo = tempo + perda_massa


print(f"\n Massa inicial: {massa}\n Massa Final: {massa_final}\n Tempo: {tempo}s")

