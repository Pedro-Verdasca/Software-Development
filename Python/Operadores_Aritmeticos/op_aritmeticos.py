#variáveis
a=10
b=3
c="8 "
d="dias"

#operadores
soma=a+b
subtracao=a-b
multiplicacao=a*b
divisao=a/b
div_inteira=a//b
modulo=a%b
potencia=a**b

concate=c+d

pot=a^b

print( )

#resultados
print(f"a + b = {soma}")
print(f"a - b = {subtracao}")
print(f"a * b = {multiplicacao}")
print(f"a / b = {divisao:.2f}")
print(f"a // b = {div_inteira}")
print(f"a % b = {modulo}")
print(f"a ** b = {potencia}")

print( )

#v2 resultados
print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao:.3f}")
print(f"{a} // {b} = {div_inteira}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {potencia}")

print( )

#concatenação
print(f"{c}+ {d} = {concate}")

print( )

#alternativa potenciação
print(f"{a} ^ {b} = {pot}")
