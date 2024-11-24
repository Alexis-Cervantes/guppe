"""
POO - PROPRIEDADES / PROPERTIES
"""
'''Em linguagens de programação, como o Java, desclaramos declaramos atributos privados nas clases, costumamos a criar
metodos púbicos para manipulação desses atributos. Esses métodos são conhecidos como Getters e Setters. Onde os getters
retornan o valor do atributo e os setters alterão o valor do atributo'''
# Exemplo 1: Ciando claase e acesasndo de forma errada

# class Conta:

#     contador = 0

#     def __init__(self, titular, saldo, limite):
#         self.__numero = Conta.contador + 1
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite
#         Conta.contador += 1

#     def extrato(self):
#         return f'saldo de: {self.__saldo} do cliente {self.__titular}'

#     def depositar(self, valor):
#         self.__saldo += valor
#
#     def sacar(self, valor):
#         self.__saldo -= valor

#     def transferir(self, valor, destino):
#         self.__saldo -= valor
#         destino.__saldo += valor

# conta1 = Conta('Alexis', 3000, 5000)
# conta2 = Conta('Duda', 2000, 4000)

# print(conta1.extrato())
# print(conta2.extrato())

# # Acesso errado dos saldos das contas.
# soma = conta1._Conta__saldo + conta2._Conta__saldo
# print(f'A soma das duas contas é: {soma}')


# Exemplo 2: Refatorando utilizando getters e setters
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'saldo de: {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

# Instanciando a classe
conta1 = Conta('Alexis', 3000, 5000)
conta2 = Conta('Duda', 2000, 4000)

# Acesso de forma correta aso saldos
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma das duas contas é: {soma}')
