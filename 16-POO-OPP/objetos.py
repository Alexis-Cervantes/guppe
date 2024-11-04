"""
POO - Objetos
- São isntancias da clase. Ou seja, após o mapeamento do objeto do mundo real para sua representação computacional,
devemos poder criar quantos objetos forem necesarios. Podemos pensar nos objetos/instâncias de uma clase como variaveis
do tipo definido na clase.
"""
# class Lampada:
#
#     def __init__(self, cor, voltagem, luminosidade):
#         self.__cor = cor
#         self.__voltagem = voltagem
#         self.__luminosidade = luminosidade
#         self.__ligada = False

    # def checa_lampada(self):
    #     return self.__ligada

    # def ligar_desligar(self):
    #     if self.__ligada:
    #         self.__ligada = False
    #     else:
    #         self.__ligada = True

# class Cliente:
#     def __init__(self, nome, cpf):
#         self.__nome = nome
#         self.__cpf = cpf

    # def diz(self):
    #     print(f'O cliente é {self.__nome} diz oi')

# class ContaCorrente:

    # contador = 4999

    # def __init__(self, limite, saldo, cliente):
    #     self.__numero = ContaCorrente.contador + 1
    #     self.__limite = limite
    #     self.__saldo = saldo
    #     self.__cliente = cliente
    #     ContaCorrente.contador = self.__numero

    # def mostra_cliente(self):
    #     print(f'O cliente é {self.__cliente._Cliente__nome}')

# class Usuario:

    # def __init__(self, nome, sobrenome, email, senha):
    #     self.__nome = nome
    #     self.__sobrenome = sobrenome
    #     self.__email = email
    #     self.__senha = senha

# Instancias/objetos:
# lamp1 = Lampada('branca', 110, 60)  # estado inicial da lampada (deslifada = False
# lamp1.ligar_desligar()  # Com esto ligamos a lampada

# print(f'A lampada esta ligada? : {lamp1.checa_lampada()}')  # Saida-> True ou false

# cc1 = ContaCorrente(5000, 20000)
# user1 = Usuario('Alexis', 'Cervantes', 'iacervantes@outlook.com', '123456')

# testando ContaCorrente e Cliente:
# cli1 = Cliente('Alexis', '123.456.789-10')
# cc = ContaCorrente(5000, 10000, cli1)
# print(cc.mostra_cliente())

# cc.mostra_cliente()
# cc._ContaCorrente__cliente.diz()    # Aceeso de forma errada

print('objetos')
