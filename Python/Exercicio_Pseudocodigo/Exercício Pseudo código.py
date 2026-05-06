#Exercício Pseudo código
#Ler nota1
#Ler nota2
#Calcule media = (nota1 + nota2) / 2
#Escrever "Média do alno é:", média
#Se media >= 7.0 então
#  Escrever "Aluno Aprovado!"
#se não
#  Escrever "Aluno Reprovado!"

nota1 = 7.5
nota2 = 6.0

media = (nota1 + nota2) / 2

print(f"A média do aluno é: {media}")

if media >= 7.0:
  print("Reprovado!")
else:
  print("Aprovado!")
