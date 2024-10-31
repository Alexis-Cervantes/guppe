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
- métodos se emcrevem com letra minuscula, e se são composto se coloca um aunderline entres ambas.
"""
from idlelib.pyshell import use_subprocess

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
        Produto.contador = self.__id

    def desconto(self, porcentagem):    # méthodo
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.encrypt(senha, rounds=200000, salt_size=16)

    def nome_completo(self):    # méthodo
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

# Criando produto ou intanciando a clase:
# p1 = Produto('Play Station 4', 'Video Game', 2300)
# print(p1.desconto(20))
# OU
# print(Produto.desconto(p1, 20)) # passamos o self, desconto

# Instanciando Usuatio:
user1 = Usuario('Alexis', 'Cervantes', 'iacervantes@outlook.com', '123456')
user2 = Usuario('Eduarda', 'Cervantes', 'madudacervantes@gmail.com', '123456')

print(user1.nome_completo())
print(user2.nome_completo())

# Acessos errados:
print(f'Senha user1: {user1._Usuario__senha}')
print(f'Senha user2: {user2._Usuario__senha}')

# Vamos a baixar uma biblioteca chamada de 'passlib' no cabeçalho da clase para ocultar a senha
nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha; ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('senha não confere')

print('Usuario criado com sucesso')
senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acessos permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografiada: {user._Usuario__senha}')
