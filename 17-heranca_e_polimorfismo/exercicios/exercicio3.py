"""3. Crie um programa, instancie um objeto da classe Carro e teste o seu méthodo."""
from exercicio2 import Carro

if __name__ == "__main__":
    carro: Carro = Carro(marca='Fiat', modelo='Palio', portas=4)

    carro.imprime()
