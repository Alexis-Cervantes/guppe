"""
Exercicios:

1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e setters para os
atributos e um méthodo para imprimir os dados de uma pessoa.

2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
    a) armazenar_contato(contato: Contato);
    b) remover_contato(contato: Contato);
    c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
    d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
    e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de forma que:
    a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
    b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
    c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também permitir que
    seja informado um número de canal para efetuar a troca;
"""
# Questão 1
class Pessoa:

    def __init__(self, nome, data_nascimento, email):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__email = email

    @property
    def nome(self):
        return f'{self.__nome}'

    @property
    def data_nascimento(self):
        return f'{self.__data_nascimento}'

    @property
    def email(self):
        return f'{self.__email}'

    def imprime_dados(self):
        print(f'Nome: {self.nome}, data de nascimento: {self.data_nascimento}, email: {self.email}')

# Questão 2
class Agenda:

    def armazenar_contato(self):
        pass
    def remover_contato(self):
        pass
    def buscar_contato(self):
        pass
    def imprimir_agenda(self):
        pass
    def imprimir_contato(self):
        pass

# Questão 3
class Televisao:
    pass

# Testando questão 1
pes1 = Pessoa('Alexis', '26/06/1974', 'iacervantes@outlook.com')
pes2 = Pessoa('Eduarda', '09-11-2008', 'madudacervantes@gmail.com')

print(pes1.nome)
print(pes1.data_nascimento)
print(pes1.email)

print(pes2.nome)
print(pes2.data_nascimento)
print(pes2.email)

Pessoa.imprime_dados(pes1)
Pessoa.imprime_dados(pes2)