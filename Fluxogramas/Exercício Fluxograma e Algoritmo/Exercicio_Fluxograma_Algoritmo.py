#Exercício Fluxograma (Escrever algoritmo)
#Nota 1 = 5.5
#Nota 2 = 6.0
#Nota 3 = 3.5
#Ler nota1
#Ler nota2
#Ler nota2
# #Calcule media = ((nota1*2) + (nota2*3) + (nota3*5))
#Escrever "Média do alno é:", média
#Se media >= 5.5 então
#  Escrever "Aluno Aprovado!"
#se não
#  Escrever "Aluno Reprovado!"

nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
nota3 = float(input("Digite a Nota 3: "))

media = ((nota1*0.2) + (nota2*0.3) + (nota3*0.5))

print(f"A média do aluno é: {media}")

if media >= 5.5:
  print("Aluno Aprovado!")
else:
  print("Aluno Reprovado!")