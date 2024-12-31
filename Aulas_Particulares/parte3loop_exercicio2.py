n = int(input('Número:'))
soma = 0
parcela = 1
sequencia = ''
while parcela <= n :
    if parcela == n: #By ERICK
      sequencia = sequencia + str(parcela)+'='
    else:
      sequencia = sequencia + str(parcela)+'+'
    soma = soma + parcela
    parcela = parcela + 1

print('Soma:', sequencia+str(soma))


soma = 0
sequencia = ''
for parcela in range(1, n+1,1) :
    if parcela == n:
      sequencia = sequencia + str(parcela)+'='
    else:
      sequencia = sequencia + str(parcela)+'+'
    soma = soma + parcela

print('Soma:', sequencia+str(soma))