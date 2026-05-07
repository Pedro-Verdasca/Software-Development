#variável global
hello="Olá"
nome="Pedro Luiz"

#função
def funcao_variaveis():
    
#variável local
saudacao="Oi"
nome="Pedro Verdasca"

print(f"\nDentro da função meu nome é: {nome}.")
print(f"\nAcessando a variável global dentro da função: {hello})


funcao_variaveis()

print(f"\n{hello}, Fora da função meu nome é {nome}")