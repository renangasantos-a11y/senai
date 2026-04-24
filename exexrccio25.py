n = int(input("Quantos produtos deseja calcular? "))

for i in range(n):
    preco = float(input("Digite o preço do produto: "))
    novo_preco = preco * 0.9
    print(f"Novo preço: R$ {novo_preco:.2f}")