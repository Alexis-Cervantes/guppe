"""Entendendo o parametro - *args"""
'''
- É um parametro como qualquer outro e que utilizado em uma função, coloca os valores extras informados como entrada
em uma TUPLA (tuplas são inutaveis).
- Você podera chama-lo de qualquer coisa, desde que começe com asterisco (*)
  Exemplo: 
  *xis
- Mas por convenção, utilizamos (*args) para defini-lo.
'''

# Exemplo: Utilzando função sem o args


def soma_todos_numeros1(num1, num2, num3):
    return num1 + num2 + num3


# print(soma_todos_numeros1(4, 6, 9))  # CERTO
# print(soma_todos_numeros1())  # TypeError porque falta passar 03 argumentos ESPERADOS
# print(soma_todos_numeros1(4))  # TypeError porque falta passar + 02 argumentos ESPERADOS
# print(soma_todos_numeros1(4, 6))  # TypeError porque falta passar + 01 argumentos ESPERADO
# print(soma_todos_numeros1(4, 6, 9, 6))  # TypeError porque passamos 01 argumentos a mais

'''Entendendo o *args'''
# Refaorando a função anterior


def soma_todos_numeros2(*args):
    print(args)


# soma_todos_numeros2()
# soma_todos_numeros2(1)
# soma_todos_numeros2(2, 3)
# soma_todos_numeros2(2, 3, 4)
# soma_todos_numeros2(3, 4, 5, 6)


def soma_todos_numeros3(*args):
    """O corpo dessa função pode se substituida tranquilamente por: return sum(args) e a função fara a mesma coisa"""
    total = 0
    for numero in args:
        total += numero
    return total


# print(soma_todos_numeros3())  # Aceita
# print(soma_todos_numeros3(1))  # Aceita 1 argumento
# print(soma_todos_numeros3(2, 3))  # Aceita 02 argumentos
# print(soma_todos_numeros3(2, 3, 4))  # Aceita 03 argumentos
# print(soma_todos_numeros3(3, 4, 5, 6))  # Aceita  04 argumentos
# print(soma_todos_numeros3('b'))  # TypeError: unsupported operand type(s) for +=: 'int' and 'str'
# print(soma_todos_numeros3(12.5, 13.6))  # Aceita FLOAT


def soma_todos_numeros4(nome, sobrenome, *args):
    return sum(args)


# print(soma_todos_numeros4('Alexis', 'Cervantes'))  # Passando valores obrigatorios. extras se vc quiser
# print(soma_todos_numeros4('Alexis', 'Cervantes', 1))  # Passando valores obrigatorios + extras
# print(soma_todos_numeros4('Alexis', 'Cervantes', 2, 3))  # Passando valores obrigatorios + extras
# print(soma_todos_numeros4('Alexis', 'Cervantes', 2, 3, 4))  # Passando valores obriga. + extras
# print(soma_todos_numeros4('Alexis', 'Cervantes', 3, 4, 5, 6))  # Passando valores obr. + extras
# print(soma_todos_numeros4('Alexis', 'Cervantes',12.5, 13.6))  # Passando valores obr. + extras

'''Otros Exemplos  utilizando args'''


def verificar_info(*args):
    if 'Alexis' in args and 'Cervantes' in args:
        return 'Bem-vindo Alexis'
    return 'Eu não tenho certeza de quem você é...'


# print(verificar_info())
# print(verificar_info(1, True, 'Cervantes', 'Alexis'))
# print(verificar_info(1, 'Cervantes', 3.145))

def soma_todos_numeros5(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

# print(soma_todos_numeros5(numeros))  # TypeError: unsupported operand type(s) for +: 'int' and 'list'

# print(soma_todos_numeros5(*numeros))  # Esse asterisco ordena desempacotar a lista. Informa a Python que estamos
# passano como argumento uma colleção. Dessa forma tera primeiro que desempacotar a coleção

print('Olá você esta no arquivo args')