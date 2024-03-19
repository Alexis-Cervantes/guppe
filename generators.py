"""Generators"""
'''
Estudamos:
- Lista Comprehension
- Dictionary Comprehension
- Set Comprehension
Não estudamos:
- Tupla Comprehension... Porque ela se chama GENERATORS
'''
# Usando 'Any': OBS: para ser um 'list Comprehension' tem que ter "Colchetes" no meio.
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))  # A saide da True ou False

# Poderiamos ter utiizado GENERATORS


