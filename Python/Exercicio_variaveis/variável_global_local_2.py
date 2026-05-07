#variáveis globais
nome="Pedro Luiz"
idade=36
altura=1.81
curso='TI'

#função
def variavel_local():

    #variáveis locais
    nome="Pedro Verdasca"
    idade=70
    altura=1.51

    print(f"(variável local) Olá, meu nome é {nome}, tenho {idade} anos de idade, {altura} de altura e sou estudante do curso de {curso}.")

variavel_local()

print(f"(variável global) Olá, meu nome é {nome}, tenho {idade} anos de idade, {altura} de altura e sou estudante do curso de {curso}.")
