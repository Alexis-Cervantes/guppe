from collections import Counter
'''https://docs.python.org/3/library/collections.html#collections.Counter'''

"""Modulo Colletions - Counter (contador)
Colletions: High-performnace Container Datetypes
Counter: Receve um iteravel como parametro e cria um objeto do tipo Colletions Counter que é parecido com um dicionario,
contendo como chave o elemento da lista pássada como parametro e como valor a quantidade de ocorrencias desse elemento.
"""
# Counter - (from collections import Counter)
# Exemplo 1: Counter e um iteravel (lista)
lista1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
# res = Counter(lista1)

# print(type(res))  # <class 'collections.Counter'>
# print(res)  # # Terminal: Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# OBS: Para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidades de ocorrencias

# Exemplo 2: - Counter com um String
# print(Counter('Alexis Cervantes'))
# terminal: Counter({'e': 3, 's': 2, 'A': 1, 'l': 1, 'x': 1, 'i': 1, ' ': 1, 'C': 1, 'r': 1, 'v': 1, 'a': 1, 'n': 1,
# 't': 1})

# Exemplo 3: - Counter e um texto
texto = """Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma orientado a 
objetos, imperativo, funcional e procedural. Possui tipagem dinâmica e uma de suas principais características é permitir
a fácil leitura do código e exigir poucas linhas de código se comparado ao mesmo programa em outras linguagens. Devido
às suas características, ela é utilizada, principalmente, para processamento de textos, dados científicos e criação de
CGIs para páginas dinâmicas para a web. Foi considerada pelo público a 3ª linguagem "mais amada", de acordo com uma
pesquisa conduzida pelo site Stack Overflow em 2018[6] e está entre as 5 linguagens mais populares, de acordo com 
uma pesquisa conduzida pela RedMonk.[7]"""

palavras = texto.split()
# print(palavras)
res = Counter(texto)
# print(res)

# Exemplo 4: Se quissemos saber o top 5 das palavras que mais ocorrencias tem - most.common(5)
# print(res.most_common(5))

print("Olá, vc esta no arquivo Collections - Counter")

