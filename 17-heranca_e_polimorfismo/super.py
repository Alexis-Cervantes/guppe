"""POO - SUPER
SUPER -> SUPER-CLASE
"""
class Animal:

    def __init__(self,nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie) # NÃO RECOMENDADO
        super().__init__(nome, especie) # RECOMENDADO
        # super().faz_som('uauuuuuu') # COM SUPER PODEMOS ATÉ MEXER DIRETO
        self.__raca = raca

# testando a clase gato
# felix = Gato('Felix', 'felino', 'angora')
# felix.faz_som('miau')

print('super')