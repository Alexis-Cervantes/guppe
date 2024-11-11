"""Exercicio 1:"""
'''1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e setters para os
atributos e um méthodo para imprimir os dados de uma pessoa.'''
from datetime import date

class Pessoa:

    def __init__(self, nome: str, data_nascimento: date, email: str) -> None: # MÉTHODO CONSTRUTOR
        self.__nome: str = nome  # Atributo
        self.__data_nascimento: date = data_nascimento    # Atributo
        self.__email: str = email    # Atributo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) ->None:
        self.__nome = nome

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        self.__data_nascimento = data_nascimento

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'Data Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}')
        print(f'E-mail: {self.email}')

# Testando questão 1
if __name__ == '__main__':
    p: Pessoa = Pessoa('Alexis Cervantes', date(1974, 6, 26) , 'iacervantes@outlook.com')
    p.imprimir()

