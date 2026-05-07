#variáveis globais
nome="Pedro Luiz"
idade=36
altura=1.81
curso='TI'

#função local
def funçao_local():

    #variáveis locais
    nome="Pedro Verdasca"
    idade=70
    altura=1.51

    print(f"(função local) Olá, meu nome é {nome}, tenho {idade} anos de idade, {altura} de altura e sou estudante do curso de {curso}.")

funçao_local()

print(f"(função global) Olá, meu nome é {nome}, tenho {idade} anos de idade, {altura} de altura e sou estudante do curso de {curso}.")