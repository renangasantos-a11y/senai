n = int(input("Quantos funcionários? "))

for i in range(n):
    salario_fixo = float(input("Digite o salário fixo: "))
    vendas = float(input("Digite o valor das vendas: "))

    comissao = vendas * 0.04
    salario_final = salario_fixo + comissao

    print(f"Comissão: R$ {comissao:.2f}")
    print(f"Salário final: R$ {salario_final:.2f}")