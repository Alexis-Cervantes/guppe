""""Doctest"""
'''
Doctests são testes que colocamos no 'docstring' das funções/metodos Python.
Para rodar um test do doctest no terminal da IDE:
Utilizamos: 'python -m doctest -v nome_do_módulo.py'

Exemplo:
(guppe) D:\codando\ahorapy\PycharmProjects\guppe> python 20-testes\doctest.py #Aqui so executamos "print(soma(3, 4)"
7
(guppe) D:\codando\ahorapy\PycharmProjects\guppe> python -m doctest -v 20-testes\doctest.py #Aqui vc executa a função
com o "doctest"
7
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctest
1 items passed all tests:
   1 tests in doctest.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

(guppe) D:\codando\ahorapy\PycharmProjects\guppe>
'''
# Exemplo 1:
# def soma(a, b):
    #"""soma os números a e b

    #>>> soma(1, 2)
    #3
    #>>> soma(4, 6)
    #10
    #"""
    #return a + b

# print(soma(3, 4)) # 7

# Exemplo 2: APLICANDO O TDD
# def duplicar(valores):
#     """duplica os valores em uma lista
#     >>> duplicar([1, 2, 3, 4])
#     [2, 4, 6, 8]

    # >>> duplicar([])
    # []

    # >>> duplicar(['a', 'b', 'c'])
    # ['aa', 'bb', 'cc']

    # >>> duplicar([True, None])
    # Traceback (most recent call last):
    #     ...
    # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    # """
    # return [2 * elemento for elemento in valores]

# Erro inesperado: ATENÇÃO o python não reconhece aspas duplas dentro do doctest

# def fala_oi():
#     """fala oi
#     >>> fala_oi()
#     'oi'
#     """
#     return "oi"

# Um uktimo caso estranho:
# def verdade():
#     """Retorne verdade
#     >>> verdade()
#     True
#     """
#     return True

print('doctest')

