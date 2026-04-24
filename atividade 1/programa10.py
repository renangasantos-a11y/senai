contador = 1
soma = 0
while contador <= 5:
    salario = float(input(f"digite o salario do {contador}funcionario: "))
    contador+= 1
    soma += salario
media = soma / 5
print("A media dos salario dos cincos funcionario é: ",media) 