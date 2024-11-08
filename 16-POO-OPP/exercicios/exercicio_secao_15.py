"""Exercicios:"""
'''1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e setters para os
atributos e um méthodo para imprimir os dados de uma pessoa.'''

class Pessoa:

    def __init__(self, nome, data_nascimento, email): # MÉTHODO CONSTRUTOR
        self.__nome = nome  # Atributo
        self.__data_nascimento = data_nascimento    # Atributo
        self.__email = email    # Atributo

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

# Testando questão 1
# pes1 = Pessoa('Alexis', '26/06/1974', 'iacervantes@outlook.com')
# pes2 = Pessoa('Eduarda', '09-11-2008', 'madudacervantes@gmail.com')
#
# print(pes1.nome)
# print(pes1.data_nascimento)
# print(pes1.email)
#
# print(pes2.nome)
# print(pes2.data_nascimento)
# print(pes2.email)
#
# Pessoa.imprime_dados(pes1)
# Pessoa.imprime_dados(pes2)

'''2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
    a) armazenar_contato(contato: Contato);
    b) remover_contato(contato: Contato);
    c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
    d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
    e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.'''

class Agenda:

    agenda = []

    def __init__(self, nome, telefone, data_nascimento):
        self.__nome = nome
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento

    def armazenar_contato(self, nome, telefone, data_nascimento, contato):
        contato = input('Digite nome do contato: ')
        self.agenda = contato
        print(f'Se agendou a: {contato}')

    def remover_contato(self):
        pass
    def buscar_contato(self):
        pass
    def imprimir_agenda(self):
        pass
    def imprimir_contato(self):
        pass

# Testando Questão 2:
cont1 = Agenda('Alexis', '(81)9-9816-2041', '26/06/1974')
cont2 = Agenda('Eduarda', '(81)9-8544-0902', '09/11/2008')
cont3 = Agenda('Cacia', '(81)9-8477-2577', '06/11/1970')

print(cont1._Agenda__nome)
print(cont1._Agenda__telefone)
print(cont1._Agenda__data_nascimento)


'''3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de forma que:
    a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
    b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
    c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também permitir que
    seja informado um número de canal para efetuar a troca;'''

class Televisao:
    pass

