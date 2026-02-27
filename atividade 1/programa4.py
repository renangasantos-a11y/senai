nome = input("Insira o nome  do aluno :")
nota1 = float(input("Insira o primerira nota :"))
nota2 = float(input("Insira o segundo nota :"))
media = (nota1 + nota2) / 2
print("Media das notas é: ", media) 
if media >= 7:
    print("O aluno esta aprovado :")
else:
     print("O aluno esta reprovado :")