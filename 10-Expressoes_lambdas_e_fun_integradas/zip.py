"""zip()"""
'''
- Ele cria um iteravel (zip object) que agrega elementos de cada uns dos iteraveis passados como entradas em pares 
'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2)

# print(zip1)  # Não podemos usar para mostrar os conteudos, porem na seguinte Seção podemos transformar em listas etc
# print(type(zip1))

# Exemplo 2: Transformando em Listas, Tuplas ou Dicionario
zip2 = zip(lista1, lista2, 'abc')
# print(list(zip2))  # Formará PARES OU TRIOS de tuplas

zip3 = zip(lista1, lista2)
# print(tuple(zip3))

zip4 = zip(lista1, lista2)
# print(set(zip4))

zip5 = zip(lista1, lista2)
# print(dict(zip5))

# Exemplo 3: OBS: zip() utiliza o menor tamanho em iteravel; Isso significa que se estiver trabalhando com iteraveis
# de tamanho diferentes, ira parar quando os elementos do menor iteravel acabar
zip6 = zip(lista1, lista2, lista3)
# print(list(zip6))

# Utilizando diferentes iteraveis com zip()
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
# print(list(zt))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# print(list(zip(*dados)))

# Exemplos mais complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final1 = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
# print(final1)

# Podemos utilizar o map():
final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
# print(dict(final2))

print('Olá, você está no arquivo Zip()')