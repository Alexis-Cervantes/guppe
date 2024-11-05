"""
POO - Abstração e Encapusulamento
O grande objetivo do POO é encapsular nosso código dentro de um grupo lógico e herárquico utilizando clases
Encapsular = cápsula

            Clases
_________________________________
|       Atributos e métodos     |
---------------------------------
Relembrando Atributos/métodos em python:
- Imagine que temos uma clase chamada Pessoa, um atributo chamado __nome e um méthodo privado chamado __falar().
- Esses elementos privados só devem/deveriam ser acessados dentro da clase. Com python acontece um fenomeno chamado
Name Mangling, que faz uma alteração na forma de se acessar os ele,entos privados, conforme:

_Clase__elemento

Exemplo - Acessando elementos fora da classe
instancia._Pessoa__nome -> acessando atributo
instancia._Pessoa__falar()  -> acessando méthodo

ABSTRAÇÃO em POO, é apenas expor dados relevantes de uma classe escondendo atributos e métodos privados de usuários.
"""
from black import validate_regex


# class Conta:

    # contador = 400

    # def __init__(self, titular, saldo, limite):
    #     self.__numero = Conta.contador
    #     self.__titular = titular
    #     self.__saldo = saldo
    #     self.__limite = limite
    #     Conta.contador += 1

    # def extrato(self):
    #     print(f'Saldo de: {self.__saldo} do titular: {self.__titular} com limite: {self.__limite}')

    # def depositar(self, valor):
    #     if valor > 0:
    #         self.__saldo += valor
    #     else:
    #         print('valor precisa ser positivo')

    # def sacar(self, valor):
    #     if valor > 0:
    #         if self.__saldo >= valor:
    #             self.__saldo -= valor
    #         else:
    #             print('Saldo insuficiente')
    #     else:
    #         print('O valor deve ser positivo')

    # def transferir(self, valor, conta_destino):
        # 1 - Remover valor da conta de origem
        # self.__saldo -= valor
        # self.__saldo -= 10 # Taixa de transferencia paga por quem realzou a transferencia
        # 2 - Adicionar o valor na conta de destino
        # conta_destino.__saldo += valor
''
# Teatando:
# conta1 = Conta('Alexis', 150.00, 1500)
# Isto funciona se os atributos estiverem publicos:
# print(conta1. numero)
# print(conta1. titular)
# print(conta1. saldo)
# print(conta1. limite)

# Como os atributoos são públicos podemos modificar eles
# conta1.numero = 42
# conta1.titular = 'xuxa'
# conta1.saldo = 9999999999999999999
# conta1.limite = 99999999999999999999999999999999999999

# print(conta1.__dict__)
# conta1.extrato()

# Python Não te barra: E acesaando desse jeito (eerado) podemos acessar
# print(conta1._Conta__titular)
# print(conta1._Conta__saldo)
# print(conta1._Conta__limite)

# Podemos modifcar informações
# conta1._Conta__titular = 'Edua

# Testando e inplemntando metodos. Dando segurança
# print(conta1.__dict__)
# conta1.depositar(150)
# print(conta1.__dict__)
# conta1.sacar(2000)
# print(conta1.__dict__)

# conta1 = Conta('Alexis', 150.00, 1500)
# conta1.extrato()

# conta2 = Conta('Eduarda', 300.00, 2000)
# conta2.extrato()

# valor = 100

# conta2.sacar(valor)
# conta1.depositar(valor)

# conta1.extrato()
# conta2.extrato()

# Teatado def transferir()
# conta2.transferir(100, conta1)
# conta1.extrato()
# conta2.extrato()

print('Abstração e encapsulamento')