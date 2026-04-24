while True:
    peso = float(input("Digite o peso da pessoa: "))

    engordar = peso * 1.15
    emagrecer = peso * 0.80

    print(f"Peso se engordar 15%: {engordar:.2f} kg")
    print(f"Peso se emagrecer 20%: {emagrecer:.2f} kg")

    opcao = input("Deseja calcular novamente? (s/n): ")
    if opcao.lower() != 's':
        break