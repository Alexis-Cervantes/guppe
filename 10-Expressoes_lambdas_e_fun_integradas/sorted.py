"""Sorted()"""

"""
- OBS1: Não confunda, a pesar do nome, com a função do sort() que já estudamos em listas. O sort() só funciona em listas  
- OBS2: Envia sempre uma nova lista com os iteraveis ordenados
- USO: Com qualquer iteravel.
- SERVE: ordenar.
"""
# Exemplo 1:
numeros_lista = [6, 1, 8, 2]
# numeros_tupla = (7, 3, 5, 8)
# numeros_set = {9, 4, 8, 10}

# print('Listas')
# print(numeros_lista)
# print(sorted(numeros_lista))  # gera nova lista
# print(numeros_lista)  # A lista original se mantem

# print('Tuplas')
# print(numeros_tupla)
# print(sorted(numeros_tupla))  # Gera nova tupla
# print(numeros_tupla)  # A tupla original se mantem

# print('sets')
# print(numeros_set)
# print(sorted(numeros_set))  # Gera novo set
# print(numeros_set)  # O set original se mantem

# Adicionanando PARAMETROS ao Sorted()
numeros = [6, 1, 8, 2]

# Impressão normal da lista:
# print('lista:')
# print(numeros)

# Impressão com Sorted(): Sem parametros
# print('sorted:')
# print(sorted(numeros))

# Podemos converter a saida na coleção que nos queranmos: Tupla, set
# print('tupla:')
# print(tuple(sorted(numeros)))  # Podmeos converter uma saide lista para tupla
# print('set: ')
# print(set(sorted(numeros)))  # Podmeos converter uma saide lista para set

# Impressão com Sorted: Com parametro 'reverse'
# print('sorted com parametro reverse: ')
# print(sorted(numeros, reverse=True))  # Ordena do maior a menor

# Podemos utilizar o Sorted com siatuações mais conplexas:
# Exemplo 1:

usuarios1 = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]

# print(usuarios1)
# print(sorted(usuarios1, key=len))

# Exemplo 2: Nos ajudaos com uma função lambda para que ele mostre de ordem ascendente> Desde quem tem mais chaves até
# quem tem manos chaves.

usuarios2 = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}
]

# print(usuarios2)

# Ordenando por 'username'
# print(sorted(usuarios2, key=lambda usuario: usuario['username']))

# Ordenando pelo numero de tweets
# print(sorted(usuarios2, key=lambda usuario: len(usuario['tweets'])))

# Ultimo Exemplo:
musicas = [{'titulo': 'Thunderstruck', 'tocou': 3},
           {'titulo': 'Dead Skin Mash', 'tocou': 2},
           {'titulo': 'Back in Black', 'tocou': 4},
           {'titulo': 'Too old to rock in roll, too young to die', 'tocou': 32}
]
# Ordenar da menos tocada hà mais tocada
# print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordenar da mais tocada hà menos tocada
# print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

print('Olá, você esta no arquivo Sorted()')