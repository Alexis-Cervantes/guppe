"""
Preservando metadata
- Metadados: São dados intrinsecos em arquivos
- Wraps: São funções que envolvem elementos com diversas finalidades

"""
# Problema:
# def ver_log(funcao):
#     def logar(*args, **kwargs):
#         """Eu sou uma função (logar) dentro de outra"""
#         print(f'Você está chamando a {funcao.__name__}')
#         print(f'Aqui a documentação: {funcao.__doc__}')
#         return funcao(*args, **kwargs)
#     return logar

# @ver_log
# def soma(a, b):
#     """Soma dois números"""
#     return a + b

# Testando:
# print(soma(10, 30))

# Verificando (__name__ e __doc__)
# print(soma.__name__)    # logar   - INFORMAÇÃO ERRADA
# print(soma.__doc__)     # Eu sou uma função (logar) dentro de outra   -INFORMAÇÃO ERRADA

# resoslução do Problema:
# from functools import wraps

# def ver_log(funcao):
#     @wraps(funcao)
#     def logar(*args, **kwargs):
#         """Eu sou uma função (logar) dentro de outra"""
#         print(f'Você está chamando a {funcao.__name__}')
#         print(f'Aqui a documentação: {funcao.__doc__}')
#         return funcao(*args, **kwargs)
#     return logar

# @ver_log
# def soma(a, b):
#     """Soma dois números"""
#     return a + b

# Testando:
# print(soma(10, 30))

# Verificando (__name__ e __doc__)
# print(soma.__name__)    # soma
# print(soma.__doc__)     #  soma dois numeros

# print(help(soma))

print('preservando matadata')