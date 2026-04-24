total_dias = int(input("Digite a quantidade de dias sem acidentes: "))

anos = total_dias // 360
resto = total_dias % 360

meses = resto // 30
dias = resto % 30

print("Tempo sem acidentes:")
print(anos, "ano(s),", meses, "mes(es) e", dias, "dia(s)")