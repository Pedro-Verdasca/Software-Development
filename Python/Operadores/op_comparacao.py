#variáveis
x=3
y=10

#operadores
maior_que=x>y
menor_que=x<y
igual_a=x==y
diferente_de=x!=y
maior_igual=x>=y
menor_igual=x<=y

#resultados
print(f"a) x > y = {maior_que}")
print(f"b) x < y = {menor_que}")
print(f"c) x == y = {igual_a}")
print(f"d) x != y = {diferente_de}")
print(f"e) x >= y = {maior_igual}")
print(f"f) x <= y = {menor_igual}")

print("---------------------------------")

#v2 resultados
#Maior que
if maior_que == True:
    print(f"a) {x} é maior que {y}? Sim") 
else:
    print(f"a) {x} é maior que {y}? Não") 

#Menor que
if menor_que == True:
    print(f"b) {x} é menor que {y}? Sim") 
else:
    print(f"b) {x} é menor que {y}? Não") 

#Igual a
if igual_a == True:
    print(f"c){x} é igual a {y}? Sim") 
else:
    print(f"c) {x} é igual a {y}? Não") 

#Diferente de
if diferente_de == True:
    print(f"d) {x} é diferente de {y}? Sim") 
else:
    print(f"d) {x} é diferente de {y}? Não")

#Maior ou igual
if maior_igual == True:
    print(f"e) {x} é maior ou igual a {y}? Sim") 
else:
    print(f"e) {x} é maior ou igual a {y}? Não")

#Menor ou igual
if menor_igual == True:
    print(f"f) {x} é menor ou igual a {y}? Sim") 
else:
    print(f"f) {x} é menor ou igual a {y}? Não")
