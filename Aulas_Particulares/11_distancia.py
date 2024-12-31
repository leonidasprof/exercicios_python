print("--"*22)
print("                 TREINA RECIFE             ")
print("                   CONVERSÃO          ")
print("--"*22)

duracao_evento = int(input(f"Digite, (inteiro), a duração em (segundos):\n\t --> "))
horas = duracao_evento // 3600
resto_hora = duracao_evento % 3600
minutos = resto_hora // 60
segundos = resto_hora % 60

print("--" * 22)
print(f"Duração  ------> {horas}h {minutos}m {segundos}s ")
print("--" * 22)