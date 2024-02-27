from collections import namedtuple
'''https://docs.python.org/3/library/collections.html#collections.namedtuple'''

"""Collections - Named Tuple"""
'''Tupla = (1, 2, 3)
named Tuple: São tuplas diferenciadas, onde especificamos um nome para elas mesmas e tamnem parametros
'''

# Importando(from collections import namedtuple)
'''Como declaramos a tupla: Presisamos definir o nome e os parametros:'''

# Forma 1: Declaração - namedtuple
cachorro1 = namedtuple('cachorro', 'idade raça nome')

# Forma 2: Declaração - namedtuple
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Fomra 3: Declaração - namedtuple
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])  # a mais entendivel

'''Como Usamos'''
nikie = cachorro3(idade=5, raca='pastor alemão', nome='Nikie')
# print(nikie)

'''Acessando dados'''
# Forme 1:
# print(nikie[0])
# print(nikie[1])
# print(nikie[2])

# Forma 2: Mais intuitiva
# print(nikie.idade)  # idade
# print(nikie.raca)  # raça
# print(nikie.nome)  # nome

# Fomra 3:
# print(nikie.index('Nikie'))  # Nikie esta no indice 2
# print(nikie.count('Nikie'))  # Nikie tem 1 ocorencia

print('Olá, você esta no arquivo namedtuple')
