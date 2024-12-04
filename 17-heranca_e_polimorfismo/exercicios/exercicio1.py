"""1. Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um méthodo para imprimir os dados de um veículo. Crie também o construtor da classe."""

class Veiculo:

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, nova_marca):
        self.__marca = nova_marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

