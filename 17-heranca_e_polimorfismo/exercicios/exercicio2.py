"""2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o méthodo de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro."""
from exercicio1 import Veiculo

class Carro(Veiculo):

    def __init__(self, portas: int, marca: str, modelo: str):
        self.__portas = portas
        super().__init__(marca)
        super().__init__(modelo)

    @property
    def portas(self) -> int:
        return self.__portas

    @portas.setter
    def portas(self, portas) -> None:
        self.__portas = portas

    def imprime(self) -> None:
