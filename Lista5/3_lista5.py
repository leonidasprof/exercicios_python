areas = []


print("__"*20)
print("           Calculo de áreas        ")
print("__"*20)
total_vendas = int(input("Total de vendas do dia:"))
print("__"*20)
for i in range(total_vendas):
    area = float(input(f"Informe a área do {i+1}º apartamento: "))
    areas.append(area)
print("__"*20)
print("              Resultados           ")
print("__"*20)
print(f"A  soma de todas as áreas é {sum(areas)}m² ")
print(f"O maior apartamento tem {max(areas)}m² de área")
print(f"O menor apartamento tem {min(areas)}m² de área")
print("__"*20)
