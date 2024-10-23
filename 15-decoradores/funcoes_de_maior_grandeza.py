"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa: Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam
otras funções como resultado o mesmo que podemos passar funções como argumento para outras funções, e até mesmo
criar variaveis do tipo de funções nos nossos programas.
OBS: No Python as funções são Cidadão de primeira clase - Firts Class Citizen

"""
# Definindo Funções Tradicinais:
# def somar(a, b):
#     return a+b


# def diminuir(a, b):
#     return a-b


# def multiplicar(a, b):
#     return a*b


# def dividir(a, b):
#     return a/b


# def calcular(num1, num2, funcao):
#     return funcao(num1, num2)

# Testando as Funções
# print(calcular(4, 3, somar))
# print(calcular(4, 3, diminuir))
# print(calcular(4, 3, multiplicar))
# print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas - Inner Functions

# Exemplo 1:
# from random import choice

# def cumprimento(pessoa):
#     def humor(): # NESTED FUNCTIO:
#         return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
#     return humor() + pessoa

# Testando
# print(cumprimento('Alexis'))
# print(cumprimento('Duda'))

# Retornando Funções de outras funções:
# def faz_me_rir():
#     def rir():
#         return choice(('hahahahaha ', 'kkkkkkkk ', 'yayayayayaya '))
#     return rir

# Testando
# rindo = faz_me_rir()
# print(rindo())

# OBS: Inner Functions (Funções Internas / Nested Functions) conseguem acessar escopos de funções mais externas
# def faz_me_rir_novamente(pessoa):
#     def dando_risada():
#         risada = choice(('hahahahaha ', 'kkkkkkkk ', 'yayayayayaya '))
#         return f'{risada} {pessoa}'
#     return dando_risada

# testando
# rindo = faz_me_rir_novamente('Eduarda')

# print(rindo())
# print(rindo())
# print(rindo())

print('Funções de maior grandeza')