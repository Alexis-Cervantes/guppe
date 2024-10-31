"""
POO - métodos
- Métodos (funções) - representam os compirtamentos do objetos. Ou seja as ações que este pode realizarno seu sistema.
- Em pythom dividimos os métodos em 2 grupos: Métodos de instancia e Métodos de clase.
- O méthodo dunder init (__init__) é um méthodo especial chamado de construtor e sua função é controir o onjeto a
partir da classe.
- Em python thodo elemento que inicia e termina com duplo underline se chama de (dunder) - dir(__builtins__)
- Os métodos/funções dunder em pythom são chamados de métodos mágicos
- Não é recomendado criar métodos/funções com duplo underline. Porque pythom cria seus me´todos desse jeito. Seu
codigo pode dar errado
"""

"""MÉTODOS DE INSTÂNCIA"""
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__liga = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha


