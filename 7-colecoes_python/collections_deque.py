from collections import deque
'''https://docs.python.org/3/library/collections.html#collections.deque'''

"""Collectios - Deque"""
'''Deque é uma lista de alta performance'''

# Criando deques:
deq1 = deque('Alexis')
# print(deq1)

# Adicionando elementos ao deque
deq1.append('c')  # adiciona ao final igual que listas
# print(deq1)

deq1.appendleft('k')  # adiciona no inicio
# print(deq1)

# Remover elementos
deq2 = deque('Cervantes')  # Remove e retorna o ultimo elemento
# print(deq2.pop())
# print(deq2)

# print(deq2.popleft())  # Remove e retorna o primeiro elemento
# print(deq2)

print('Olá, você esta no arquivo Deque')
