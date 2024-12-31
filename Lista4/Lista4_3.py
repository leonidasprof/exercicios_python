import os
os.system('cls')

def sequencia(x):
    for i in range(1, x+1):
        print(i, end=" ")
    print()

while True:
    x = int(input("Informe um número."))
    if x != 0:
        sequencia(x)
    else:
        break