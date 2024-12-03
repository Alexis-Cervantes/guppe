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

class Pinguim(Terrestre, Aquatico):
    def  __init__(self, nome):
        super().__init__(nome)

