class NPS:
    def __init__(self):
        self.notas = []

    def adicionar_notas(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print('Nota inválida!\nInsira uma nota entre 0 e 10:')
            
    def calcular_nps(self):
        # Descobrir a quantidade de detratores
        detratores = len([n for n in self.notas if n < 7])
        # Descobrir a quantidade de promotores
        promotores = len([n for n in self.notas if n >= 9])
        
        # calcular percentual de Detratores e Promotores
        percentual_detratores = (detratores / len(self.notas)) * 100
        percentual_promotores = (promotores / len(self.notas)) * 100
        
        # calcular o NPS
        nps = percentual_promotores - percentual_detratores
        return nps
    
    def exibir_classificacao(self):
        nps = self.calcular_nps()
        
        if nps >= 75:
            print("Zona de Excelência")
        if nps >= 50:
            print("Zona de Qualidade")
        elif nps >= 0:
            print("Zona Neutra")
        else:
            print("Zona Crítica")
           
avaliacao = NPS()

avaliacao.adicionar_notas(10)
avaliacao.adicionar_notas(8)
avaliacao.adicionar_notas(7)
avaliacao.adicionar_notas(9)
avaliacao.adicionar_notas(5)
avaliacao.adicionar_notas(7)
avaliacao.adicionar_notas(3)
avaliacao.adicionar_notas(-5)
avaliacao.adicionar_notas(0)
avaliacao.adicionar_notas(6)

print(avaliacao.calcular_nps())
avaliacao.exibir_classificacao()


