salario = float(input("Digite o salário: "))

aumento = salario * 0.15
salario_com_aumento = salario + aumento

imposto = salario_com_aumento * 0.08
salario_final = salario_com_aumento - imposto

print("Salário inicial: R$", salario)
print("Salário com aumento: R$", salario_com_aumento)
print("Salário final: R$", salario_final)