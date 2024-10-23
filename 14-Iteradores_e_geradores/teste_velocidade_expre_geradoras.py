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

# Exemplos
print(sum(num for num in range(1, 4)))
