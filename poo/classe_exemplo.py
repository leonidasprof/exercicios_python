class MinhaClasse:
    pass

class Carro:
    n_rodas = 4
    
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor
   
sentra = Carro("sedan", 2.0)
#corolla = Carro()
fox = Carro("hatch", 1.0)

print(sentra.modelo)
print(sentra.n_rodas)
print(sentra.motor)

print(fox.modelo)
print(fox.n_rodas)
print(fox.motor)

