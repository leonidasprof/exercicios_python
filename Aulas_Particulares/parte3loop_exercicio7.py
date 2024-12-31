qt_num = 0
soma_num = 0
media_num = 0
pares = 0

for i in range (4):
    num = float(input(f"Digite o {i+1}º número: "))
    if num == 999:
        break
    num = int(num)
    if num % 2 == 0:
        pares += num
    soma_num = soma_num + num

qt_num = i+1
media_num = (pares / qt_num)

print(f"\n Soma dos números pares: {pares}\n A quantidade digitada foi: {qt_num}\n A média dos pares é: {media_num}\n A soma dos números digitados é: {soma_num}")
