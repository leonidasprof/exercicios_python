popa = float(input('POPA:'))
popb = float(input('POPB:'))
anos = 0

while popa < popb :
    popa = popa + (popa * 3/100)
    popb = popb + (popb * 1.5/100)
    anos = anos + 1

print(f'Qtd de Anos: {anos}anos')