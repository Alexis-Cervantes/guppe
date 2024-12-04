"""
POO - POLIMORFISMO
Objetos que podem se comportar de formas diferentes

Quando reimplementamos um méthodo presenta na classe pai em clases filhas estamos realizando uma sobrescrita de
méthodo - OVERRIDING

Overriding é a mellhor representação de POLIMORFISMO
"""
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A clase filha (quem esta herdando), precisa implementar este MÉTODO')

    def comer(self):
        print(f'{self.__nome} esta comendo...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo...')
# Teatando:
felix = Gato('Felix')
# felix.comer()
# felix.falar()

pluto = Cachorro('Pluto')
# pluto.comer()
# pluto.falar()

mickey = Rato('Mickey')
# mickey.comer()
# mickey.falar()

print('POLIMORFISMO')