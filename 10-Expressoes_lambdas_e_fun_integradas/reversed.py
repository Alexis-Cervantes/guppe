"""Reversed"""
'''
OBS: Não confnunda com a função reverse() que estudamos em Listas 
- A função reverse() so funciona em listas. 
- A função reversed() funciona com quaquer iteravel
- Sua função é enverter o iteravel
- Ela retorna um iteravel chamado List Reverse Iterator
'''
# Exemplo 1:
lista = [1, 2, 3, 4, 5]
res = reversed(lista)

# print(res)
# print(type(res))

# Podemos convertir esse resultado em: Lista, tupla ou conjunto

# lista
# print(list(reversed(lista)))

# tupla
# print(tuple(reversed(lista)))

# conjunto(set)
# print(set(reversed(lista)))  # Em conjuntos, não definimos a ordem dos elementos

# Podemos iterar sobre o reversed
# for letra in reversed('Alexis Cervantes'):
    # print(letra, end='')

# print('\n')

# Podemos fazer o mesmo se a ajuda do for: Invertendo string (reversed('Alexis Cervantes'). Depois transformando essa
# string em uma lista (list(reversed('Alexis Cervantes'))). E por ultimo transformando essa lista em strin ''.join
# print(''.join(list(reversed('Alexis Cervantes'))))

# Já vimos como fazer isso mais facil com a 'slice' de strings
# print('Alexis Cervantes'[::-1])

# Podemos rambem utilizar o reversed() para fazer um loop for reverso
# for n in reversed(range(0, 10)):
    # print(n)

# A pesar que tambem já vimos como fazer isso utilzando o proprio range()
# for n in range(9, -1, -1):
    # print(n)

print('Olá você está no arquivo reversed')