"""
Forçando tipo de dados com decoradores
"""

# def forcar_tipo(*tipos):
#     def decorador(funcao):
#         def converte(*args, **kwargs):
#             novo_args = []
#             for(valor, tipo) in zip(args, tipos):
#                 novo_args.append(tipo(valor))
#             return funcao(*novo_args, **kwargs)
#         return converte
#     return decorador

# @forcar_tipo(str, int)
# def repete_msg(msg, vezes):
#     for vez in range(vezes):
#         print(msg)

# teatando repete_msg:
# repete_msg('alexis', '3')

# @forcar_tipo(float, float)
# def dividir(a, b):
#     print(a/b)

# testando def dividir():
# dividir('1', 5)

print('Forçando tipos')
