"""Min e Max"""
'''
max() -> Retorna o MAIOR valor de um iteravel ou o maior de dois ou mais elementos
min() -> Retorna o MINIMO valor de um iteravel ou o manor de dois ou mais alementos 
'''
lista = [1, 8, 4, 99, 34, 129]
# print(max(lista))  # 129
# print(min(lista))  # 1

tupla = (1, 8, 4, 99, 34, 129)
# print(max(tupla))  # 129
# print(min(tupla))  # 1

conjunto = {1, 8, 4, 99, 34, 129}
# print(max(conjunto))  # 129
# print(min(conjunto))  # 1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
# print(max(dicionario.values()))  # 129
# print(min(dicionario.values()))  # 1

# Outras formas de interagir com Max():
# Exemplo 1: Faça um programa que receve 02 valores de um usurio e mostre o maior
# val1 = int((input('Informe o primeiro valor: ')))
# val2 = int((input('Informe o Segundo valor: ')))
# print(max(val1, val2))

# Exemplo 2: Faça um programa que receve 02 valores de um usurio e mostre o menor
# val3 = int((input('Informe o primeiro valor: ')))
# val4 = int((input('Informe o Segundo valor: ')))
# print(min(val3, val4))

# # Exemplo 3:
# print(max(4, 67, 54))
# print(min(4, 67, 54))

# print(max('a', 'ab', 'abc'))
# print(min('a', 'ab', 'abc'))

# print(max('a', 'b', 'c', 'g'))
# print(min('a', 'b', 'c', 'g'))

# print(max(3.145, 3.789))
# print(min(3.145, 3.789))

# print(max('Alexis Cervantes'))  # x
# print(min('Alexis Cervantes'))  # espaçõ em branco

# Outros Exemplos
nomes = ('Arya', 'Samson', 'Dora', 'Tim', 'Ollivander')
# print(max(nomes))  # Leva em conta a ordem alfabetica (Tim)
# print(min(nomes))  # Leva em conta a ordem alfabetica (Arya)

# Alterando o comportamento de MAX e MIN. Podemos definir pela quantidade de letras
# print(max(nomes, key=lambda nome: len(nome)))
# print(min(nomes, key=lambda nome: len(nome)))

# Copiado de Sorted
musicas = [{'titulo': 'Thunderstruck', 'tocou': 3},
           {'titulo': 'Dead Skin Mash', 'tocou': 2},
           {'titulo': 'Back in Black', 'tocou': 4},
           {'titulo': 'Too old to rock in roll, too young to die', 'tocou': 32}
]
# print(max(musicas, key=lambda musica: musica['tocou']))
# print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO 1: Imprima o nome da música mas e menos tocada
# print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
# print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO 2: Como encontrar a musica MAIS e MENOS tocada sem usar (max(), min() e lambda):
'''OBS: É MAS TRABALHOSO FAZER ESSA TECNICA'''
# max = 0
# for musica in musicas:
#     if musica['tocou'] > max:
#         max = musica['tocou']
#
# for musica in musicas:
#     if musica['tocou'] == max:
#         print(musica['titulo'])
#
# min = 99999
# for musica in musicas:
#     if musica['tocou'] < min:
#         min = musica['tocou']
#
# for musica in musicas:
#     if musica['tocou'] == min:
#         print(musica['titulo'])

print('Olá, você está no arquivo Min() e Max()')