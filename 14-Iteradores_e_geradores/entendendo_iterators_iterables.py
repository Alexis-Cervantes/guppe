"""
Entendendo Iterators e Iterables
Iterator ->
        - Um objeto que pode ter iterado
        - Um objeto que retorna um dado, sendo um elemento por vez quando uma função 'next()' é chamada.
Iterable ->
        - Um objeto que ira retornar um iterator quando a função 'iter()' for chamada.
"""

# Entndo diferenças:
# nome e data são iterables porem não são iterators
# nome = 'Alexis'
# data = [1, 9, 7, 4]

# Testando essas variaveis - iterables
# print(nome)
# print(data)

# Testando esses iterables com função 'next()' - Va dar Erro
# print(next(nome))  # TypeError: 'str' object is not an iterator
# print(next(data))  # TypeError: 'int' object is not an iterator

# Transformando as variaveis iterables com iter() para ser chamadas pela função 'next()'
# iter1 = iter(nome)
# iter2 = iter(data)

# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))

# print(next(iter2))
# print(next(iter2))
# print(next(iter2))
# print(next(iter2))

# Vamos ver como atua por baixo dos panos: usando loop for - O paython faz o seguinte:
# Python aplica a função 'iter()' a 'nome' e quando imprime aplica a função 'next()' a letra. E ele automaticamemte
# para quando não tem mais caratere
# for letra in nome:
#     print(letra)

print('Entendo iterators e iterables')