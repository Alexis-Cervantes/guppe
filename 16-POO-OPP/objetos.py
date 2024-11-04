"""
POO - Objetos
- São isntancias da clase. Ou seja, após o mapeamento do objeto do mundo real para sua representação computacional,
devemos poder criar quantos objetos forem necesarios. Podemos pensar nos objetos/instâncias de uma clase como variaveis
do tipo definido na clase.
"""
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False

    def checa_lampada(self):
        return self.ligada

    def liga_desligar(self):
        if

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.numero = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.__numero

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

# Instancias/objetos:
lamp1 = Lampada('branca', 110, 60)
cc1 = ContaCorrente(5000, 20000)
user1 = Usuario('Alexis', 'Cervantes', 'iacervantes@outlook.com', '123456')



