"""POO - Herença / Inheritance"""
'''A ideia de herença é a da reaproveitar código. Tambem extener as nossas clases.
OBS: Com a herança, a partir de uma classe existente, nos extendemos outra classe que passa a herdar atributos da classe
herdada
EX:

Cliente:
- nome;
- sobrenome;
- cpf;
- renda; 

Funcionario:
- nome;
- sobrenome;
- cpf;
- matricula;
OBS: Existe alguma entidade generica o suficiente para emcapsular os atributose métodos comuns a outras entidades?

A classe herdada é cpnhecida como:
[Pessoa]
- Super Classe;
- Classe Mãe;
- Classe Pai;
- Classe Base;
- Classe Genérica;

A classe que herda é conhecida como:
[Cliente], [Funcionario]
- Sub Classe
- Classe Filha
- Clase Especifica 
'''
# MOMENTO INCIAL - sem utilização de heránça
# class Cliente:
#
#     def __init__(self, nome, sobrenome, cpf, renda):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#         self.__renda = renda
#
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'
#
# class Funcionario:
#
#     def __init__(self, nome, sobrenome, cpf, matricula):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#         self.__matricucla = matricula
#
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'
#
#
# cliente1 = Cliente('Alexis', 'Cervantes', 70247526452, 1300)
# funcionario1 = Funcionario('Eduarda', 'Cervantes', 70165412382, 5000)
#
# print(cliente1.nome_completo())
# print(funcionario1.nome_completo())

# MOMENTO SEGUNDO - utilização de herença
# class Pessoa:
#
#     def __init__(self, nome, sobrenome, cpf):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'
#
# class Cliente(Pessoa):
#     """Cliente herda de Pessoa"""
#     def __init__(self, nome, sobrenome, cpf, renda):
#         Pessoa.__init__(self, nome, sobrenome, cpf) # Tambem podemos trabalhar desse jeito
#         # super().__init__(nome, sobrenome, cpf)
#         self.__renda = renda
#
# class Funcionario(Pessoa):
#     """Funcionario herda de Pessoa"""
#     def __init__(self, nome, sobrenome, cpf, matricula):
#         super().__init__(nome, sobrenome, cpf)
#         self.__matricucla = matricula
#
#
# cliente1 = Cliente('Alexis', 'Cervantes', 70247526452, 1300)
# funcionario1 = Funcionario('Eduarda', 'Cervantes', 70165412382, 5000)
#
# print(cliente1.nome_completo())
# print(funcionario1.nome_completo())
#
# # Vamos verificar de onde ven as informações:
# print(cliente1.__dict__)
# print(funcionario1.__dict__)

# OVERRIDING
"""Sobreescrita de métódo ocorre quando reimplementamos (reescrevemos) um metódo presenta na Super Classe em classe
filha"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Tambem podemos trabalhar desse jeito
        # super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Overriding
    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'

# Sobreescrita de métodos ou (overriding)
# cliente1 = Cliente('Alexis', 'Cervantes', 70247526452, 1300)
# funcionario1 = Funcionario('Eduarda', 'Cervantes', 70165412382, 5000)

# print(cliente1.nome_completo())
# print(funcionario1.nome_completo())


print('herança')