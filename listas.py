"""LISTAS"""

'''Listas em Python funcioman como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
 DINAMICO, e tambem de podermos colocar QUALQUER tipo de dado
 
 Linguagens C e Java: Arrays
  -  Possue tamanho e tipo de dado fixo
     Ou seja nestas lingugens se vc criar um array de tipo inteiro e com tamanho 5, este array SEMPRE sera 
     do TIPO inteiro e podera ter SEMPRE o maximo de 5 valores.
     
PYTHON:
 - DINAMICO: Não possuem tamanho fixo: - podemos criar as listas e simplesmenste ir adicionando elementos
 - QUALQUER TIPO DE DADO: Não possue tipo de dado fixo -  podemos colocar qualquer tipo de dado.
 - As listas são represetadas por colchetes: [].
'''
# # print([])
# type([])
#
lista1 = [13, 76, 21, 94, 5, 3, 100, 11]
# print(lista1)
lista2 = ['a', 'b', 'c', 'd']
# print(lista2)
lista3 = []
# print(lista3)
lista4 = list(range(11))
# print(lista4)
lista5 = list('Alexis')
# print(lista5)

'''Podemos verificar se determinado valor esta contido na lista - in'''
# if 3 in lista1:
#     print('Encontrei o numero 3')
# else:
#     print('Não encontreo numero 3')

'''Podemos ordenar nossa lista - sort()'''
# lista1.sort()
# print(lista1)

'''Podemos contar o numero de ocorrencias de um valor numa lista - count()'''
# print(lista1.count(94))
# print(lista5.count('x'))

'''Podemos adicionar elementos (valores) em listas - append()'''
# Exemplo 1:
# print(lista1)
# print(lista1.append(1000))
# print(lista1)

# Exemplo 2:
'''OBS: append adiciona um elemento por vez. Porem aceita adicionar varios valores dentro de um (01) elemento de tipo
 lista'''
# print(lista1)
# lista1.append([25, 36, 64])
# print(lista1)

# Exemplo 3: procurando a lista inserida - in
# if [25, 36, 64] in lista1:
#     print('Encontre a lista')
# else:
#     print('Não encontrei a lista')

# Exemplo 4: procurando uma outra lista que não esta dentro de uma lista
# if [13, 76, 21] in lista1:
#     print('Encontre a lista')
# else:
#     print('Não encontre a lista')

# Exemplo 5: Adiciona elementos individuais na lista - extend()
'''OBS: Com extend podemos adicionar varios valores individuais de vez. Não aceita valores unicos. Aaceita iteraveis'''
# lista1.extend([51, 21, 61])
# print(lista1)

# Exemplo 6: POdemos inserir um valor novo informando a posição. append() e extend()
'''OBS: O novo elemento não substitui o valor anterio, ele é empurrado para direita. Posição 3 indice'''
# lista1.insert(2, 'novo_valor')
# print(lista1)

# Exemplo 7:Podemos juntar duas listas
# lista6 = lista1 + lista2
# print(lista6)

# Exemplo 8: O extend faz o mesmo que o anterio
# lista1.extend(lista2)
# print(lista1)

# Exmplo 9: Estilo elemento = elemento + 1
# lista1 = lista1 + lista2
# print(lista1)

# Exmplo 10: Inverter ordem das listas
# lista1.reverse()
# lista2.reverse()
# print(lista1)
# print(lista2)

# Exemplo 11: Inverter ordem das listas com (::-1)
# print(lista1[::-1])
# print(lista2[::-1])

# Exemplo 12: copiar listas
# lista6 = lista2.copy()
# print(lista6)

# Exemplo 13: contar elementos em uma lista - len(lista)
# print(len(lista1))
# print(len(lista2))
# print(len(lista3))
# print(len(lista4))

# Exemplo 14: Podemos remover o ultimo elemento de uma lista - Alem de remover tambem retorna o elemento retirado
# print(lista5)
# lista5.pop()
# print(lista5)

# Exemplo 15: Podemos remover um elemento pela sua posição - os elementos a direita saõ deslocados para esquirda
# OBS: Se não houver elemento no indice teremos o erro IndexErro
# lista5.pop(2)
# print(lista5)

# Exmplo 16: POdemos zerar a lista
# print(lista5)
# lista5.clear()
# print(lista5)

# Exmplo 17: Podemos repetir elementos em uma lista
# nova = [1, 2, 3]  # criamos nova lista
# print(nova)
# nova = nova * 3
# print(nova)

# Exemplo 18: Podemos convertir uma string para uma lista - split()
# OBS: split separa os elementos que existe entre elas
# lema1 = 'Arriba Alianza Lima'
# print(lema1)
# lema1 = lema1.split()
# print(lema1)

# Exemplo 19: Podemos especificar os elementos de separação entre as strings
# lema2 = 'Arriba,Alianza,Lima'
# print(lema2)
# lema2 = lema2.split(',')
# print(lema2)

# Exemplo 20: Convertendo uma lista em uma string
# lista6 = ['Ismael', 'Alexis', 'Cervantes', 'Negreiros']
# print(lista6)

# Exemplo 20.1: Pega a lista6 e coloca um espaço entre cada elemento e transforma em uma strig
# curso = ' '.join(lista6)
# print(curso)

# Exmplo 20.2: Pega a lista6 e coloca um $ entre cada elemento e transforma em uma string
# curso = '$'.join(lista6)
# print(curso)

# Exemplo 21: Podemos colocar qualquer tipo de dado em uma lista. Inclusive misturando esse tipo de dados
lista7 = [1, 2.34, True, 'Alexis', 'd', [1, 2, 3], 5050505050]
# print(lista7)
# print(type(lista7))

# Exemplo 22: Iterando sobre listas - FOR
# for elemento in lista4:
#     print(elemento)

# Exemplo 22.1:
# soma = 0
# for elemento in lista4:
#     print(elemento)
#     soma += elemento
# print(soma)

# Exemplo 22.2:
# soma = ''
# for elemento in lista2:
#     print(elemento)
#     soma += elemento
# print(soma)

# Exemplo 23 - Iteerando sobre lsitas - while
carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)