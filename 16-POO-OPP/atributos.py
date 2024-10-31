"""
POO - Atrubutos
- Representan as carateristicas do objeto. Ou seja, pelos atributos nos conseguimos representar computacionalmente
os estados de um objeto

Em python, dividimos os atributos em tres grupos:
- Atributos de Instância
- Atributos de Classe
- Atributos Dinãmicos

OBS: Méthodo Construtor: é um méthodo especial utilizado para a construção de objetos

JAVA: uma clase Lampada incluido os seus atributos ficaria mais ou menos assim:

public class Lampada(){
    private int coltagem;
    public String cor;
    protected Boolean ligada = false;

    public Lampada(int voltagem, String cor){   (# MÉTHODO CONSTRUTOR DO JAVA)
        this.coltagem = voltagem;
        this.cor = cor;
    }
    public int getVoltagem():{  # è necesrio criar esse metodos para ter acesso aos atributos do metodo costrutor
        return this.voltagem
    }
}
# OBS: Por convenção que thodo atributo de uma clase é publico. Ou seja pode ser acessado em thodo o projeto. Caso se
# queremos que um atributo seja tratado como privado, ou seja que deve ser acessado denro da propria clase onde esta
# declarado, utiliza-se (__) duplo underline no inicio do nome.
# Isso é conhecido como Name Mangling

"""
'''Atributos de instancia: São atributos que são declarados dentro do metodo CONSTRUTOR'''
# PYTHON: avanzado - atributos de instancia privado (__)
# class Lampada:
#     def __init__(self, voltagem, cor):  # MÉTHODO CONSTRUTOR
#         self.__voltagem = voltagem  # __ seria o private do java
#         self.__cor = cor
#         self.__ligada = False

    # @property   # è necesrio criar esse metodos para ter acesso aos atributos do metodo costrutor
    # def voltagem(self):
    #     return self.__voltagem

    # @property   # è necesrio criar esse metodos para ter acesso aos atributos do metodo costrutor
    # def cor(self):
    #     return self.__cor

    # @property
    # def ligada(self):
    #     return self.__ligada

# Python: básico - atributos de instancia publicos sem (__)
# OBS: Vemos que o primeiro atributo é 'self'. Significa que 'self' representa o proprio objeto. Exemplo
# O Objeto Usuario no atributo nome vai receber nome e asim por diante

# class ContaCorrente:

    # def __init__(self, numero, limite, saldo):
    #     self.numero = numero
    #     self.limte = limite
    #     self.saldo = saldo

# class Produto:

    # def __init__(self, nome, descricao, valor):
    #     self.nome = nome
    #     self.descricao = descricao
    #     self.valor = valor

# class Usuario:

    # def __init__(self, nome, email, senha):
    #     self.nome = nome
    #     self.email = email
    #     self.senha = senha

# Atributos Públicos e Atributos Privados - Visibilidade
# class Acesso:

    # def __init__(self, email, senha):
    #     self.email = email  # atributo publico
    #     self.__senha = senha    # atributo privado

    # def mostra_senha(self):
    #     print(self.__senha)

    # def mostra_email(self):
    #     print(self.email)

# OBS: Lembrando que é so uma convensão. O python não vai impedir que façamos acesso aos atributos sinalizados como
# privado fora da clase.

# Exemplo:
# user = Acesso('user@mail.com', 123456)
# print(user.email)
# print(user.__senha) # ttributeError: 'Acesso' object has no attribute '__senha' - nivel basico de segurança do python

# Otimizando
# print(dir(user))   #-> SAIDA ['_Acesso__senha', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'email']

# CUIDADO!! -> '_Acesso__senha'
# Então o hacker ve isso e aceesa mediante esse porta de entrada
# print(user._Acesso__senha)  # -> Saida 123456 / temos acesso mas não devetiamos acessar desse jeito. Name Mangling

# Se queremos visualizar a senha: Implimentar, dentro da clase Acesso, um atributo que mostre
# user.mostra_senha()
# user.mostra_email()

# O que sig=gnifica atributos de instancia:
# Signfica que ao criarmos instancias/objetos de uma clase, todas as instancias terão esse atributos

# user1 = Acesso('alexis@gmail.com', 123456)
# user2 = Acesso('negra@hotmail.com', 608248)

# user1.mostra_email()
# user2.mostra_email()

'''Atributos de Clase: '''
"""
São atributos que são declarados diretamente na clase, ou seja, fora do COSTRUTOR. Geralmente já inicializamos um valor
e esse valor é compartilhado entre todas as instâncias da clase. Ou seja, ao invés que cada instância de clase ter seus
proprios valores como é o caso dos atributos de instância, com os atributos de clase todas as instâncias terão os mesmo
valores para esse atributo.  
"""
# class Produtos:
    # Atributo de clase
    # imposto = 1.05 # 0.05 % de imposto
    # contador = 0

    # def __init__(self, nome, descricao, valor):
    #     self.id = Produtos.contador + 1
    #     self.nome = nome
    #     self.descricao = descricao
    #     self.valor = (valor*Produtos.imposto)
    #     Produtos.contador = self.id

# p1 = Produtos('PlayStation 4', 'Video game', 2300 )
# p2 = Produtos('Xbox 5', 'Video game', 4500 )

# print(p1.valor) # 2415.0 -  porem incorreto acesso
# print(p2.valor) # 4725.0 -  Porem incorreto acesso

# OBS: Não precisamos criar uma instância de uma clase para fazer acesso a um atributo de clase
# print(Produtos.imposto)

# testando o contador e o id
# print(p1.id)
# print(p2.id)

# OBS: Em java os atributos de clase (python) são chamados atributos estáticos.

'''Atributos Dinâmicos: '''
"""
Atributo de instância que pode ser criado em tempo de execução; e ele é exclusivo da instancia que o criou.
"""
# class Produts:
    # Atributo de clase
    # imposto = 1.05 # 0.05 % de imposto
    # contador = 0

    # def __init__(self, nome, descricao, valor):
    #     self.id = Produts.contador + 1
    #     self.nome = nome
    #     self.descricao = descricao
    #     self.valor = (valor*Produts.imposto)
    #     Produts.contador = self.id

# p1 = Produts('PlayStation 6', 'Video game', 2200 )
# p2 = Produts('Arroz', 'Mercearia', 5.99 )

# Criando um atributo dinâmico em tempo de execução:
# p2.peso = '5Kg'
# p1.peso = '3Kg'# Note que na calse products não exite o atributo peso
# print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos
# aantes de deletar
# print(p1.__dict__)
# print(p2.__dict__)

# Acessando a Clase Products:
# print(Produts.__dict__) # Saisa-> {'__module__': '__main__', 'imposto': 1.05, 'contador': 2, '__init__': <function
# Produts.__init__ at 0x0000022A01DC51C0>, '__dict__': <attribute '__dict__' of 'Produts' objects>, '__weakref__':
# <attribute '__weakref__' of 'Produts' objects>, '__doc__': None}

# deletando:
# depois de deletar
# del p2.peso
# del p1.peso
# del p2.valor
# del p2.descricao

# print(p1.__dict__)
# print(p2.__dict__)

print('atributos - poo')