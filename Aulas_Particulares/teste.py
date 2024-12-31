n = int(input())
entrada = input().split()
a,b = entrada[0], entrada[1]
a,b = int(a), int(b)
soma_presentes = a +b
if soma_presentes <= n:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")