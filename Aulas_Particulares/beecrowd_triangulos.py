valores = input()
lados = list(map(float, valores.split()))

#Ordenar os lados em ordem decrescente
lados.sort(reverse=True)
A, B, C = lados[0], lados[1], lados[2]
# Verificar se forma um triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Verificar tipo de ângulo
    if A ** 2 == B ** 2 + C ** 2:
        print("TRIANGULO RETANGULO")
    elif A ** 2 > B ** 2 + C ** 2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    # Verificar tipo de lados
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")



