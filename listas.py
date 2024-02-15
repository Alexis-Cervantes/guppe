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

'''Podemos verificar se determinado valor esta contido na lista'''
# if 3 in lista1:
#     print('Encontrei o numero 3')
# else:
#     print('Não encontreo numero 3')

'''Podemos facilmente ordenar nossa lista'''
# lista1.sort()
# print(lista1)

'''Podemos facilmente contar o numero de ocorrencias de um valor numa lista'''
# print(lista1.count(94))
# print(lista5.count('x'))

'''Podemos facilmente adicionar elementos (valores) em listas com a função "append
OBS: Com append so conseguimos adicionar um elento por vez. Porem se podemos adicionar um elemento de tipo lista"'''
# Exemplo 1:
# print(lista1)
# print(lista1.append(1000))
# print(lista1)

# Exemplo 2:
print(lista1)
lista1.append([25, 36, 64])
print(lista1)

# Exemplo 3:
if [25, 36, 64] in lista1:
    print('Encontre a lista')
else:
    print('Não encontrei a lista')