"""
Decorators com diferentes assinaturas
- Assinatura de uma função é representanda pelo seu retorno, nome e parametros de entrada
"""
# Decorators Function:
# def gritar(funcao):
#     def aumentar_tamanho_letras(nome):
#         return funcao(nome).upper()
#     return aumentar_tamanho_letras

# Testando 1: função saudacao() decorada pela função gritar()
# @gritar
# def saudacao(nome):
#     return f'Olá, eu sou, o/a {nome}'

# print(saudacao('Alexis'))

# Testando 2: função ordenar() decorada pela função gritar()
# @gritar
# def ordenar(principal, acompanhamento):
#     return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento},, por favor'
#
# print(ordenar('Picanha', 'batata Frita'))
# Saida TypeError: gritar.<locals>.aumentar_tamanho_letras() takes 1 positional argument but 2 were given

# Refatorando a Função ordenar: Decoartor Pattern
def gritar(funcao):
    def aumentar_tamanho_letras(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar_tamanho_letras

# Testando 1: função saudacao() decorada pela função gritar()
# @gritar
# def saudacao(nome):
#     return f'Olá, eu sou, o/a {nome}'
#
# print(saudacao('Alexis'))

# Testando 2: função ordenar() decorada pela função gritar()
# @gritar
# def ordenar(principal, acompanhamento):
#     return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'

# print(ordenar('Picanha', 'batata Frita'))

# vale lembrar que podemos utilizar parametros nomeados:
# print(ordenar(acompanhamento='batata Frita', principal='picanha'))

# Decorator com Argumentos:
# def verifica_primeiro_argumento(valor):
#     def interna(funcao):
#         def outra(*args, **kwargs):
#             if args and args[0] != valor:
#                 return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
#             return funcao(*args, **kwargs)
#         return outra
#     return interna

# @verifica_primeiro_argumento('pizza')
# def comida_favorita(*args):
#     print(args)
# Testando comida_favorita:
# print(comida_favorita('pizza', 'locro'))


# @verifica_primeiro_argumento(10)
# def soma_dez(num1, num2):
#     return num1 + num2
# # Testando soma_dez
# print(soma_dez(10, 5))

print('desoradores com assinatura')