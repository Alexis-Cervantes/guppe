"""List Comprehension - parte 1"""

'''
- Utilizando list comprhension, nos podemos gerar novas listas com dados processados a partir de outra iteravel
- Sintaxe: 
  [dado for dado in iteravel]
- Vemos que se utilizam colchetes [ ] na Sintaxy'''

# Exemplo 1:
numeros1 = [1, 2, 3, 4, 5]

res1 = [numero * 10 for numero in numeros1]
# print(res1)

res3 = [numero / 2 for numero in numeros1]
# print(res3)
"""
- Primera parte: for numero in numeros
- Segunda parte: numero * 10
"""
# Exemplo 2:
numeros2 = [1, 2, 3, 4, 5]


def funcao(valor):
    return valor * valor


res2 = [funcao(numero) for numero in numeros2]
# print(res2)

# List Comprenhension vs

# LOOP
numeros3 = [1, 2, 3, 4, 5]  # lista
numeros_dobrados3 = []  # Lista vazia

for numero in numeros3:  # Para cada numero em numeros3
    numero_dobrado = numero * 2  # cria uma variavel que receva numero * 2
    numeros_dobrados3.append(numero_dobrado)  # depois acrecenta a variavel numeros_dobrados a variavel numero_dobrado

# print(numeros_dobrados3)

# Refatorando o lopp
numeros_dobrados4 = []

for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados4.append(numero * 2)

# print(numeros_dobrados4)


# List comprehensions
# print([numero * 2 for numero in numeros3])

# refatorando a list comprenhension
# print([numero * 2 for numero in [1, 2, 3, 4, 5]])

# Outros Exemplos
# 1: Convertir las primeiras letras dos nomes da lista em maiusculo
nome = 'Alexis Cervantes'
# print([letra.upper() for letra in nome])

#

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
# print([caixa_alta(amigo) for amigo in amigos])

# 3: Multiplicar um valor * 3 no rabgo entre 1 e 10
# print([numero * 3 for numero in range(1, 10)])

# 4: Converter os valores da lista que esta a direita do for em boolean. Utilizando o 'cast'
# print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5: Converter um valor numerico em string utilizando o 'cast'
# print([str(numero) for numero in [1, 2, 3, 4, 5]])

print('Olá você esta no arquivo list Comprehension')
