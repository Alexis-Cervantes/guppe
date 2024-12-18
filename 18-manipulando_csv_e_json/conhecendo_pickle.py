"""Conhecendo o PICKLE"""
from encodings import normalize_encoding

'''A função do PICKLE é realizar a seguinte função
- Objeto Python  -> Binarização
- Binarização -> Objeto Python
Esse processo se chama serialização/deserialização
OBS: O modo PICKLE não é tão seguro com dados maliciosos e desta forma não é recomendado trabalhar com arquivos PICKLE
vindo de outras pessoas que você não conheça ou de fonte desconhecida'''

import pickle

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} esta comendo...')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} esta miando...')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo...')

# Instanciando:
felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Escrita de arquivos PICKLE
# with open('animais.pickle', 'wb') as arquivo:
#     pickle.dump((felix, pluto), arquivo)

# Leitura de dados de arquivos PICKLE
# with open('animais.pickle', 'rb') as arquivo:
#     gato, cachorro = pickle.load(arquivo)
#     print(f'O gato chama-se {gato.nome}')
#     gato.mia()
#     print(f'O tipo de gato é {type(gato)}')
#
#     print(f'O cachorro chama-se {cachorro.nome}')
#     cachorro.late()
#     print(f'O tipo de cachorro é {type(cachorro)}')

print('Arquivo PICKLE')