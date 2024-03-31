"""Set Comprehension - (Conjuntos - set)"""
'''
lista = [1, 2, 3, 4]
conjunto = {1, 2, 3, 4}
'''
# Exemplo 1
numeros1 = {num for num in range(1, 7)}
# print(numeros1)

# Exemplo 2
numeros2 = {x ** 2 for x in range(10)}
# print(numeros2)

# DESAFIO: faça uma alteração no exemplo 2 para gerar um dicionario ao invés de set:
numeros3 = {x: x ** 2 for x in range(10)}
# print(numeros3)

# Exemplo 3: String
letras = {letra for letra in 'Alexis Cervantes'}
# print(letras)  # Sem ordenação e sem repetição

print('Olá você está no arquivo Set Comprehension')