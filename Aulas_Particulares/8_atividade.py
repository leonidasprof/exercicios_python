print("--"*18)
print("              TREINA RECIFE             ")
print("                CONCURSO           ")
print("--"*18)


total_homens = int(input(f"Digite a quantidades de homens que participaram:"))
total_mulheres = int(input("Digite a quantidades de mulheres que participaram: "))
total_ausentes = int(input("Digite a quantidades de ausentes: "))
total_participantes = total_ausentes + total_homens + total_mulheres
print("--" * 18)
print(f"O percentual de homen foi  ------>{(total_homens*100)/total_participantes} ")
print(f"O percentual de mulheres foi:\n -------> R${(total_mulheres*100)/total_participantes} ")
print(f"O percentual de ausentes foi:\n -------> R${(total_mulheres*100)/total_participantes} ")
print("--" * 18)