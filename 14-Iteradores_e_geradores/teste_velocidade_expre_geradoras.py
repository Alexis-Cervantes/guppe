"""
Teste de velocidade com expressões geradoras
"""
from types import new_class
# Diferença:

# GENERATOR:
# def nums():
#     for num in range(1, 10):
#         yield num

# ge1 = nums()    # GENERATOR
# print(ge1)

# testndo:
# print(next(ge1))
# print(next(ge1))

# GENERATORS EXPRESSION:
# ge2 = (num for num in range(1, 10))

# print(ge2)  # GENERATOR EXPRESSION

# Teatando:
# print(next(ge2))
# print(next(ge2))

# Outros Exemplos de teste de velocidade:
# import time

# gen_inicio = time.time()
# print(sum(num for num in range(10000))) # 1000  -> 0.0011157989501953125 - MAIS EFICIENTE
# gen_tempo = time.time() - gen_inicio

# List Comprehension
# list_inicio = time.time()
# print(sum([num for num in range(10000)])) # 1000 -> 0.0011441707611083984 - ESTUVO CERCA DE LA OTRA
# list_tempo = time.time() - list_inicio

# print(f'Generators Expression levou: {gen_tempo}')
# print(f'List Comprehension levou: {list_tempo} ')

print('teste de velocidade com expreções geradoras')