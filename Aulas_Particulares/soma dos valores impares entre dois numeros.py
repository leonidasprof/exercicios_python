#opção_1
X = int(input())
Y = int(input())
X, Y = min(X, Y), max(X, Y)
numeros = list(range(X + 1, Y))
impares = [num for num in numeros if num % 2 != 0]
soma = sum(impares)
print(soma)

#opção_2
'''X, Y = sorted(map(int, input().split()))
soma = sum(num for num in range(X + 1, Y) if num % 2 != 0)
print(soma)

#opção_3
print(f"{sum(num for num in range(*((lambda x: (x[0] + 1, x[1]))(sorted(map(int, input().split()))))) if num % 2 != 0)}")'''










