"""Erros mais comuns em Python"""
'''
- ATENÇÃO!: É importante prestar atenção e aprender a ler as saidas de erros geradas pela execução de nosso codigo
- Os erros mais comuns:'''

'''
1.- SyntaxError -> O python encontra um erro de sintaxe. Ou seja você escreveu algo que o Python não reconhece como 
parte da linguagem.

a)
def funcao:
    print('Alexis')   
    
SyntaxError: expected '('             

b)
def = 1

SyntaxError: invalid syntax

c)
return

SyntaxError: 'return' outside function'''

'''
2.- NameError -> Quando uma função ou variavel não foi definida.

a)
print(Alexis)

NameError: name 'Alexis' is not defined

b)

a = 8  # Se alteramos este valor que seja maior que 10. A saida sera um NameErro
msg = 'Utilizamos esta string para evitar a saida de NameErro - algo'

if a < 10:
    msg = 'É menor que 10'

print(msg)

NameError: name 'msg' is not defined
'''

'''
3.- TypeError: Quando uma operação/função/ação é aplicado a um tipo errado
 
 a)
print(len(5))
TypeError: object of type 'int' has no len()

b)
print(len('Alex' + [])'''

'''
4.- IndexError -> Quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um indice
invalido. 

a)
lista = ['alex']
print(lista[2])

IndexError: list index out of range'''


'''
5.- ValueError -> Quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor 
inapropriado

a)

print(int('alex'))

ValueError: invalid literal for int() with base 10: 'alex' '''

'''
6.- KeyError -> Tentamos acessar um dicionarios com uma chave que não existe

a)

dicionario = {}  # dicionario = {'Nome': 'Alexis'} - Se implementamos esse dicionario com sua chave e seu valor.
                                                    Nãoa dara erro. Agora se eo inves de 'Nome' colocamos outro valor
                                                    dara erro de novo
print(dicionario['Nome'])

KeyError: 'Nome'''

'''
7.- AttributeError -> Quando uma variavel não tem um atributo/função
a)

tupla = (11, 2, 31, 4)
print(tupla.sort())  # sort() é uma função da lista e não da tupla. Por isso mostra error

AttributeError: 'tuple' object has no attribute "sort" '''

'''
8.- IndentationError -> Quando não respeitamos a indentação do Python (4 espaços)
a)
def funcao():
print('Alexis')

IndentationError: expected an indented block after function definition on line 104'''

"""
OBS: Exceptions e Erros são sinonimos na programação
OBS: Importante ler e prestar atenção na saida de erro
"""

print('Olá você está no arquivo Erros mais comuns')
