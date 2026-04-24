total = float(input("Digite o valor total da conta: "))

parte = int(total / 3)  # tira os centavos

carlos = parte
andre = parte

felipe = total - (carlos + andre)

print("Carlos paga: R$", carlos)
print("André paga: R$", andre)
print("Felipe paga: R$", felipe)