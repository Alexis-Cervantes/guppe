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
 LISTAS SÃO MUTAVEIS
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
# carrinho = []
# produto = ''
# while produto != 'sair':
#     print('Adicione um produto na lista ou digite "sair" para sair: ')
#     produto = input()
#     if produto != 'sair':
#         carrinho.append(produto)
#
# for produto in carrinho:
#     print(produto)

# Exemplo 24 - Criando listas - Utilizando variaveis em listas
numeros1 = [1, 2, 3, 4, 5]
# print(numeros1)
#
# num1 = 1
# num2 = 2
# num3 = 3
# num4 = 4
# num5 = 5
#
# numeros2 = [num1, num2, num3, num4, num5]
# print(numeros2)

# Exemplo 25 - Em listas acessamos os elementos de forma indexada
# index     0        1         2        3
cores1 = ['verde', 'amrelo', 'azul', 'branco']

# print(cores1[0])  # VERDE
# print(cores1[1])  # AMARELO
# print(cores1[2])  # AZUL
# print(cores1[3])  # BRANCO

# Exemplo 26 - Acessando ao indeice de forma inversa - OBS: Neste caso pense na lista como uma roda
# index     0        1         2        3
cores2 = ['verde', 'amrelo', 'azul', 'branco']

# print(cores2[-1])  # BRANCO
# print(cores2[-2])  # AZUL
# print(cores2[-3])  # AMARELO
# print(cores2[-4])  # VERDE

# Exemplo 27 - FOR
cores3 = ['verde', 'amrelo', 'azul', 'branco']

# for cor in cores3:
#     print(cor)

# Exemplo 27 - WHILE
cores4 = ['verde', 'amrelo', 'azul', 'branco']
# indice = 0
# while indice < len(cores4):
#     print(cores4[indice])
#     indice += 1

# Exemplo 28 - Gerar um indice em um for
cores5 = ['verde', 'amrelo', 'azul', 'branco']
# for indice, cor in enumerate(cores5):
#     print(indice, cor)

# Exemplo 29 - Listas aceitam valores repetidos
lista8 = []
# lista8.append(26)
# lista8.append(21)
# lista8.append(12)
# lista8.append(12)
# lista8.append(26)
# print(lista1)

# Exemplo 30 - Outros metodos não tão importahtes
# Encontrar o indice de um elemento na lista
numeros3 = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista esta o valor 6?
# print(numeros3.index(6))

# Em qual indice da lista esta o valor 9?
# print(numeros3.index(9))

# Duplicidade de elementos - Retrona o indice do primeiro elemento encontrado
# print(numeros3.index(5))

# Podemos fazer busca dentre um rango. Ou seja qual indice começar buscar
# print(numeros3.index(5, 1))  # Buscar a partir do indice 1
# print(numeros3.index(5, 2))  # Buscar a partir do indice 2
# print(numeros3.index(5, 3))  # Buscar a partir do indice 3
# print(numeros3.index(5, 4))  # Buscar a partir do indice 4
# OBS: Caso não tenha ese elemento na lista. Sera apresentado um erro: ValueError

# Podemos fazer busca dentre um rango. Inicio/fim
# print(numeros3.index(8, 3, 6))  # Buscar indice do valor 8 dentre os indeices 6 a 8

'''REVISÃO DE SLICING
# listas[inciio:fim:passo]
# range[inciio:fim:passo]'''
lista9 = [1, 2, 3, 4]

# Trabalhando com slice de listas com o parametro incio:
# print(lista9[1:])  # iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de listas com o parametro fim:
# print(lista9[:2])  # começa do indice 0 pega ate o indice 2 - 1
# print(lista9[1:3])  # começa do indice 1 pega ate o indice 3 - 1

# Trabalhando com slice de listas com o parametro passo:
# print(lista9[1::2])  # começa do indice 1 vai  até o final de 2 em 2
# print(lista9[::2])  # começa do indice 0 vai  até o final de 2 em 2

#  Invertindo valores em uma lista
# nomes1 = ['Alexis', 'Eduarda']
# nomes1[0], nomes1[1] = nomes1[1], nomes1[0]
# print(nomes1)

# Modo Pytonico:
# nomes2 = ['Cacia', 'Magaly']
# nomes2.reverse()
# print(nomes2)

'''Soma, Valor Máximo, Valor Mínimo, Tamanho'''
# lista10 = [1, 2, 3, 4, 5, 6]
# print(sum(lista10))  # Soma
# print(max(lista10))  # Maximo valor
# print(min(lista10))  # Minimo valor
# print(len(lista10))  # tamanho de elementos

'''Convertir uma lista em tupla'''
# lista11 = [1, 2, 3, 4, 5, 6]
# print(lista11)
# print(type(lista11))
#
# tupla = tuple(lista11)
# print(tupla)
# print(type(tupla))

'''Desempacotando uma lista'''
# lista12 = [1, 2, 3]
# num1, num2, num3 = lista12
#
# print(num1)
# print(num2)
# print(num3)
# OBS: Se tivermos um numero diferente de elementos na lista o variaveis para receber os dadoas ValeuError

'''Copiado uma lista para outra - Shallow Copy e Deep Copy'''
# Forma 1:
# lista13 = [1, 2, 3]  # CRIAMOS LISTA13
# print(lista13)  # IMPRIMIMOS A LISTA13
#
# nova_lista13 = lista13.copy()  # COPIAMOS A LISTA13 PARA UMA NOVA LISTA (NOVAS_LISTA13)
# print(nova_lista13)  # IMPRIMIMOS A NOVA_LISTA13
#
# nova_lista13.append(26)  # ACRESENTAMOS O NUMERO 26 A NOVA_LISTA13
#
# print(lista13)  # IMPRIMIMOS LISTA13
# print(nova_lista13)  # IMPRIMIMOS NOVA_LISTA13
'''OBS: DEEP COPY (Copia profunda): Observamos que quando copiamos (lista13.copy) os valores de uma lista (lista13) para
outra variavel/lista (nova_lista13). As duas ficaram idependentes, isto é, a ação de modificarmos uma lista não afeta
a outra'''

# Forma 2:
lista14 = [1, 2, 3]  # CRIAMOS LISTA14
# print(lista14)  # IMPRIMIMOS A LISTA14

nova_lista15 = lista14  # 'ATRIBUIMOS' OS VALORES DA LISTA14 PARA UMA NOVA LISTA (NOVA_LISTA15)
# print(nova_lista15)  # IMPRIMIMOS A NOVA_LISTA15

nova_lista15.append(26)  # ACRESENTAMOS O NUMERO 26 A NOVA_LISTA15

# print(lista14)  # IMPRIMIMOS LISTA14
# print(nova_lista15)  # IMPRIMIMOS NOVA_LISTA15
'''OBS: SHALLOW COPY: Observamos que realizamos a atribuição dos valores da lista14 a uma nova variavel/lista 
(nova_lista15). Depois quando realizamos a ação de modificar a lista (append(26), esta ação refleteuse em ambas as 
listas'''

print('Olá, voce está no arquivo LISTAS...')
