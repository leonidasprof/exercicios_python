idade = int(input('Digite sua idade: '))

if idade<16:
    print("Voce não pode votar!")

elif idade>=18 and idade<71:
    print("Você é obrigado a votar!")

else:
    print("Voto opcional! ")