"""Dictionary Comprehension"""

'''
- Se quisermos criar uma lista (List):
  lista = [1, 2, 3, 4, 5]

- Se quisermos criar uma Tupla (Tuple):
  tupla = (1, 2, 3, 4, 5)  # 1, 2, 3, 4, 5

- Se quisermos criar uma Conjunto (Set):
  conjunto = {1, 2, 3, 4, 5}

-  Se quisermos criar uma Dicionario (Dict):
  dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

- Sintaxe:
  {chave: valor for valor in iteravel}
'''
# Exemplo 1:
numeros1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado1 = {chave: valor ** 2 for chave, valor in numeros1.items()}
# print(quadrado1)

# Exemplo 2:
numeros2 = [1, 2, 3, 4, 5]  # Lista
numeros3 = (1, 2, 3, 4, 5)  # Tupla
numeros4 = {1, 2, 3, 4, 5}  # Set

quadrado2 = {valor: valor ** 2 for valor in numeros2} # Lista
# print(quadrado2)

quadrado3 = {valor: valor ** 2 for valor in numeros3} # Tupla
# print(quadrado3)

quadrado4 = {valor: valor ** 2 for valor in numeros4} # Set
# print(quadrado4)

# Exemplo 3:
numeros5 = [1, 2, 3, 4, 5, 1, 2]  # Lista com 2 numeros repetidos
quadrado5 = {valor: valor ** 2 for valor in numeros2}
# print(quadrado5)  # Não existe numero repetidos

# Exemplo 4:
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(len(chaves))}
# print(mistura)

# Exemplos com logica condicional
numeros6 = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros6}
# print(res)

print('Olá você está no arquivo dictioanry comprhension')