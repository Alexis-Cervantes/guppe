"""
POO - MRO - METHOD RESOLUTION ORDER
Resolução de ordem de Métodos - é a ordem da execução dos metodos - quem será executado primeiro
Em Python: se pode conferir os (MRO) de 3 formas
- Vía propriedade da classe _mro_
- Vía Méthodo mro()
- Vía help()
"""
# Vamos reutilizar código da seção - herença multipla
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
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Terrestre, Aquatico): # A ordem entre Terrestre/Aquatico definira as informações de saida
    def  __init__(self, nome):
        super().__init__(nome)

# Testando:
tux = Pinguim('Tux')
# print(tux.cumprimentar())   # saida -> Eu sou Tux da terra

'''
Pinguim(Aquatico, Terrestre)
Eu sou Tux do mar!

Pinguim(Terrestre, Aquatico)
Eu sou Tux da Terra!
'''

print('mro')