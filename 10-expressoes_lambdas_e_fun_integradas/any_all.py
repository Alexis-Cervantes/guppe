"""Any and All"""

'''
All(): Retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio.
'''
# Exemplo: All
# print(all([0, 1, 2, 3, 4]))  # Todos os elementos são verdadeiros?. Não todhos, o zero é FALSE. Então resultado é FALSE
# print(all([1, 2, 3, 4]))  # Todos os elementos são verdadeiros?. Sim, O resultado True
# print(all([]))  # Todos os elementos são verdadeiros?. Lista vazia é True
# print(all((0, 1, 2, 3, 4)))  # Tupla: Todos os elementos são verdadeiros?.
# print(all({0, 1, 2, 3, 4}))  # Set: Todos os elementos são verdadeiros?.
# print(all('Alexis'))  # Todos os elementos são verdadeiros?.

# Exemplo 2:
nomes1 = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
# print(all([nome[0] == 'C' for nome in nomes1]))

# Exemplo 3:
nomes2 = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']
# print(all([nome[0] == 'C' for nome in nomes2]))

# Exemplo 4:
# print(all([letra for letra in 'eio' if letra in 'aeiou']))

# Exemplo 5: Um iteravel vazio convertido em boolean é false, mas o all() entende como True
# print(all([letra for letra in 'gju' if letra in 'pok']))

# Exemplo 6: True
# print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])) # True
# print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1])) # true porque gera lista vazia

'''
Any(): Retorna True se qualquer elemento do iterável for verdadeiro. Se o iteravel estiver vazio retorna False
'''
# Exemplo 1:
# print(any([0, 1, 2, 3, 4]))  # True
# print(any([0, False, {}, (), []]))  # False

# Exemplo 2:
nomes3 = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
# print(any([nome[0] == 'C' for nome in nomes3]))  # True

# Exemplo 3:
nomes4 = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
# print(any([nome[0] == 'C' for nome in nomes4]))  # True

# Exemplo 4:
# print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0])) # True

print('Olá você esta no arquivo Any and All')