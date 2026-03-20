pao = int(input("digite a quantidade de pao vendido "))
broa = int(input("digite a quantidade de broa vendidos "))

arrecadado = (pao * 0.12) + (broa * 1.50)
poupança = (arrecadado * 0.10)

print("total de vendas de pao e broa foi: ", arrecadado)
print("quantidade e dinheiro que ira para poupança: ",poupança)