from collections import OrderedDict
'''https://docs.python.org/3/library/collections.html#collections.OrderedDict'''

"""Modulo Collections - Ordered Dict"""
'''Em um dicionario a ordem de inserção de elementos não é garantida
OrderedDict: É um dicionario que nós garante a ordem de inserção dos elementos'''
# dicionario1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# print(dicionario1)
#
# for chave, valor in dicionario1.items():
#     print(f'chave={chave}:valor={valor}')

# Fazendo o import (from collections import OrderedDict)
dicionario2 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
# for chave, valor in dicionario2.items():
#     print(f'chave={chave}: valor={valor}')

'''Diferença entre Dict e OrderedDict'''
# Dicionarios Comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

# print(dict1 == dict2)  # True: Já que a ordem dos elementos não importam para o diconarios

# OrderedDict:
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
# print(odict1 == odict2)  # False: Já que a ordem dos elementos se importam para o OrderedDict

print('Olá, você esta no arquivo Collections - OrderedDict')

