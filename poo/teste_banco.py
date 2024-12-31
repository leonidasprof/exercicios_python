class ContaBancaria:
    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")
        

conta_Ananda = ContaBancaria("Ananda", 1000.000)
conta_Bruna = ContaBancaria("Bruna", 200.00)

conta_Ananda.exibir_saldo()
conta_Ananda.depositar(500.00)
conta_Ananda.exibir_saldo()
conta_Ananda.sacar(2000.00)
conta_Ananda.exibir_saldo()