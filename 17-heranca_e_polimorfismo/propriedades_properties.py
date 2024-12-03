"""
POO - PROPRIEDADES / PROPERTIES
"""
from dis import RETURN_CONST

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


# Exemplo 2: Refatorando a classe utilizando funções com comportamentos 'getters' e 'setters'
# class Conta:
#
#     contador = 0
#
#     def __init__(self, titular, saldo, limite):
#         self.__numero = Conta.contador + 1
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite
#         Conta.contador += 1
#
#     def extrato(self):
#         return f'saldo de: {self.__saldo} do cliente {self.__titular}'
#
#     def depositar(self, valor):
#         self.__saldo += valor
#
#     def sacar(self, valor):
#         self.__saldo -= valor
#
#     def transferir(self, valor, destino):
#         self.__saldo -= valor
#         destino.__saldo += valor
#
#        # Funções com comportamentos Geteers e Setters
#
#     def get_numero(self):
#         return self.__numero
#
#     def get_titular(self):
#         return self.__titular
#
#     def set_titular(self, titular):
#         self.__titular = titular
#
#     def get_saldo(self):
#         return self.__saldo
#
#     def set_saldo(self, saldo):
#         self.__saldo = saldo
#
#     def get_limite(self):
#         return self.__limite
#
#     def set_limite(self, limite):
#         self.__limite = limite
#
# # Instanciando a classe
# conta1 = Conta('Alexis', 3000, 5000)
# conta2 = Conta('Duda', 2000, 4000)
#
# print(conta1.extrato())
# print(conta2.extrato())
#
# # Acesso de forma correta aso saldos
# soma = conta1.get_saldo() + conta2.get_saldo()
# print(f'A soma das duas contas é: {soma}')
#
# """Criar getter e setters como a criamos liha acima é tipico do Java. getters são faceis de manipular, porem os seters
# são perigossos pela função de mexer com valores ou modificar valorers"""
#
# # Exemplo usando setters criados:
# print(conta1.__dict__)
# conta1.set_limite(9999999)
# print(conta1.__dict__)

# Exemplo 3: Refatorando a classe utilizando Propriedades
# class Conta:
#
#     contador = 0
#
#     def __init__(self, titular, saldo, limite):
#         self.__numero = Conta.contador + 1
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite
#         Conta.contador += 1
#
#     @property
#     def numero(self):
#         return self.__numero
#
#     @property
#     def titular(self):
#         return self.__titular
#
#     @property
#     def saldo(self):
#         return self.__saldo
#
#     @property
#     def limite(self):
#         return self.__limite
#
#     @limite.setter
#     def limite(self, novo_limite):
#         self.__limite = novo_limite
#
#
#     def extrato(self):
#         return f'saldo de: {self.__saldo} do cliente {self.__titular}'
#
#     def depositar(self, valor):
#         self.__saldo += valor
#
#     def sacar(self, valor):
#         self.__saldo -= valor
#
#     def transferir(self, valor, destino):
#         self.__saldo -= valor
#         destino.__saldo += valor

#    # Criando um property

#    @property
#    def valor_total(self):
#        return self.__saldo + self.__limite

# Instanciando a classe
# conta1 = Conta('Alexis', 3000, 5000)
# conta2 = Conta('Duda', 2000, 4000)

# print(conta1.extrato())
# print(conta2.extrato())

# Acesso de forma correta aso saldos
# soma = conta1.saldo + conta2.saldo
# print(f'A soma das duas contas é: {soma}')

# Alterando os valores do limite com o @linite.setter - conta1
# print(conta1.__dict__)
# conta1.limite = 76543
# print(conta1.__dict__)
# print(conta1.limite)

# Testando a propertie criada (valor_total) - detalhe uma função demandaria a inclusão de parentesis tipo: valor_total()
# Mas como é prooriedade então não va
# print(conta1.valor_total)
# print(conta2.valor_total)

print('Properties')