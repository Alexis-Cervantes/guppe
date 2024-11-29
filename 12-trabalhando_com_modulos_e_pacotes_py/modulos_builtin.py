"""Trabalhando com modulos Builtin (Módulos integrados, que já bem instalados no python)"""
'''
__________________________
|Python | Modulos Builtin | 
__________________________
Reeferencias: https://docs.python.org/3/py-modindex.htmlx'
'''
# Importando o modulo random:
# import random  # Importa todas as funções do modulo
# print(random.random())  # Se chama Modulo(random).função(random())

# Criando um alias para os modulos/funçoes 1:
# import random as rdm
# print(rdm.random())  # Ele já não obedece o nome Modulo 'Random'. Agora ele mudou de nome para Modulo(rdm)

# Criando um alias para os modulos/funçoes 2:
# from random import randint as rdt
# print(rdt(5, 89))  # Ele já não obedece o nome da função 'randint'. Ele mudou de nome para função(rdt)

# Criando um alias para os modulos/funçoes 3:
# from random import randint as rdt, random as rdm
# print(rdt(5, 89))  # Ele já não obedece o nome da função 'randint'. Ele mudou de nome para função(rdt)
# print(rdm(5, 89))  # Ele já não obedece o nome da função 'random'. Ele mudou de nome para função(rdm)

# Podemos importar todas as funções de um módulo utilizando *
# from random import *  # importabdo todas as funções do Modulo
# print(random())

# Para chamar multiples funções de um mesmo modulo podemos utilizarmos as tuplas:
# from random import (
#     random,
#     randint,
#     shuffle,
#     choice
# )

# print(random())
# print(randint(3, 7))
# lista = ['Alexis', 'Cervantes', 'Negreiros']
# shuffle(lista)
# print(lista)
# print(choice('Cervantes'))

print('Olá vc esta no arquivo Modulos built-in')