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
'''
# MOMENTO INCIAL
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


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, renda):
        self.__renda = renda

class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, matricula):
        self.__matricucla = matricula


cliente1 = Cliente('Alexis', 'Cervantes', 70247526452, 1300)
funcionario1 = Funcionario('Eduarda', 'Cervantes', 70165412382, 5000)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
