quantidade = int(input("Digite a quantidade de sanduíches: "))

queijo = quantidade * 100
presunto = quantidade * 50
carne = quantidade * 100

queijo_kg = queijo / 1000
presunto_kg = presunto / 1000
carne_kg = carne / 1000

print("Quantidade necessária:")
print("Queijo:", queijo_kg, "kg")
print("Presunto:", presunto_kg, "kg")
print("Carne:", carne_kg, "kg")