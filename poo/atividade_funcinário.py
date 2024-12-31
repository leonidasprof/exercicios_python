class Funcionario:
    def __init__(self, matricula, nome, salario):
        print(f"Informções do Colaborador")
        print("--" * 36)
        self.matricula = matricula
        self.nome = nome
        self.__salario = salario
        self.historico_aumentos = []

    # privado
    def salario(self):
        return self.__salario

    # regra negócio
    def salario(self, valor):
        if valor >= self.__salario:
            self.__salario = valor
        else:
            print("Não é possível definir um salário menor que o atual")

    def aumentar_salario(self, percentual):
        aumento = self.__salario * percentual / 100
        novo_salario = self.__salario + aumento
        self.__salario = novo_salario
        self.historico_aumentos.append((percentual, novo_salario))

    def exibir_informacoes(self):
        print(f"Matrícula: {self.matricula}, Nome: {self.nome}, Salário Atual: R$ {self.__salario:.2f}")
        print("--" * 36)
        print("Histórico de Aumentos:\n")
        for percentual, novo_salario in self.historico_aumentos:
            print(f"Percentual: {percentual}% -> Salário Atual: R$ {novo_salario:.2f} Salário Anteror: {novo_salario - (novo_salario*percentual/110):.2f}")

# Exemplo de uso
funcionario = Funcionario(1, "João Silva", 3000)
funcionario.aumentar_salario(10)
funcionario.aumentar_salario(5)
funcionario.exibir_informacoes()
