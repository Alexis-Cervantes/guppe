"""Exercicio 2:"""
'''2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
    a) armazenar_contato(contato: Contato);
    b) remover_contato(contato: Contato);
    c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
    d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
    e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.'''
from datetime import date
from exercicio_1_secao_15 import Pessoa

class Agenda:

    def __init__(self):
        self.__contatos: list[Pessoa] = []

    @property
    def contatos(self)-> list[Pessoa]:
        return self.__contatos

    def armazenar_contato(self, contato: Pessoa)-> None:
        self.__contatos.append(contato)

    def remover_contato(self, contato: Pessoa) -> None:
        self.__contatos.remove(contato)

    def buscar_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} esta na posição {indice}')

    def imprimir_agenda(self)-> None:
        for contato in self.contatos:
            contato.imprimir()

    def imprimir_contato(self, indice: int)-> None:
        self.contatos[indice].imprimir()

# Testando Questão 2:
if __name__ == '__main__':
    ct1: Pessoa = Pessoa('Alexis Cervates', date(1974, 6, 26), 'iacervantes@outlook.com')
    ct2: Pessoa = Pessoa('Eduarda Cervantes', date(2008, 11, 9), 'madudacervantes@gmail.com')
    ct3: Pessoa = Pessoa('Cacia Morais', date(1970, 11, 6), 'cacia6@hotmail.com')

    agenda: Agenda = Agenda()

    # Armazenar contato
    agenda.armazenar_contato(ct1)
    agenda.armazenar_contato(ct2)
    agenda.armazenar_contato(ct3)

    # Imprimir agenda:
    agenda.imprimir_agenda()

    # Buscar contato:
    agenda.buscar_contato('Alexis Cervantes')

    # Imprimir contato - indice
    agenda.imprimir_contato(0)

    # remover contato
    agenda.remover_contato(ct3)

    # Imprimir agenda
    agenda.imprimir_agenda()
