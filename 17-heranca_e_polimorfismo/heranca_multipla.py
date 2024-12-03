"""
POO - HERANÇA MULTIPLA
Herwnçza multipla não é mas do que uma classe herdar de multiplas classes, fazendo com que a classe filha herde todos
os atributos e métodos das classes herddas
OBS: A herença multipla pode ser feita de duas maneiras:
- Por MULTIDERIVAÇÃO DIREITA
- Por MULTIDERIVAÇÃO INDIRETA
"""
# Exemplo 1: Multiderivação Direta
# class Base1:
#     pass

# class Base2:
#     pass

# class Base3:
#     pass

# class Multiderivada(Base1, Base2, Base3):
#     pass

# Exemplo 2: Multiderivação Indireta
# class Base1:
#     pass

# class Base2(Base1):
#     pass

# class Base3(Base2):
#     pass

# class Multiderivada(Base3):
#     pass

# Exemplo real
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'

class Pinguim(Terrestre, Aquatico): # A ordem entre Terrestre/Aquatico definira as informações de saida
    def  __init__(self, nome):
        super().__init__(nome)

# Testando:
baleia = Aquatico('Nilie')
# print(baleia.nadar())
# print(baleia.cumprimentar())

tatu = Terrestre('Colmen')
# print(tatu.andar())
# print(tatu.cumprimentar())

tux = Pinguim('Alberto')
# print(tux.andar())
# print(tux.nadar())
# print(tux.cumprimentar()) # 'Eu sou Alberto da terra' / 'Eu sou Alberto do mar' - MRO: Method Resolution Order

# Objeto é instancia de..
# print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
# print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
# print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
# print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')
# print(f'Tux é instância de Object? {isinstance(tux, object)}')

print('Herença multipla')