num_extenso = {
    "0": "zero", "1": "um", "2": "dois", "3": "três", "4": "quatro", 
    "5": "cinco", "6": "seis", "7": "sete", "8": "oito", "9": "nove",
    "zero": "0", "um": "1", "dois": "2", "três": "3", "quatro": "4", 
    "cinco": "5", "seis": "6", "sete": "7", "oito": "8", "nove": "9"
}


def converter(numero):
    return num_extenso[numero]


entrada = input()

for i in range (0,10):
    if entrada == "":
        print(converter(entrada))
    


'''
while True:
    try:
        entrada = input()
        if entrada == "":
            break
        print(converter(entrada))
    except EOFError:
        break'''