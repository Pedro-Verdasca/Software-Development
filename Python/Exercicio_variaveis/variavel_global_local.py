#variável global
hello_global="Olá"
nome="Pedro Luiz"

#função
def funcao_variaveis():
    
#variável local
    hello_local="Oi"
    nome="Pedro Verdasca"
    print(f"\n{hello_local}, dentro da função, meu nome é: {nome}.")
    print(f"\nAcessando a variável hello_global dentro da função: {hello_global}.")

funcao_variaveis()


print(f"\n{hello_global}, fora da função, meu nome é {nome}")
