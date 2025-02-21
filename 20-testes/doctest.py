""""Doctest"""
'''
Doctests são testes que colocamos no 'docstring' das funções/metodos Python.
Para rodar um test do doctest no terminal da IDE:
Utilizamos: 'python -m doctest -v nome_do_módulo.py'

Exemplo:
(guppe) D:\codando\ahorapy\PycharmProjects\guppe> python 20-testes/doctest.py
7
(guppe) D:\codando\ahorapy\PycharmProjects\guppe> python -m doctest -v  20-testes/doctest.py
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

def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)
    3
    >>> soma(4, 6)
    10
    """

    return a + b

print(soma(3, 4)) # 7