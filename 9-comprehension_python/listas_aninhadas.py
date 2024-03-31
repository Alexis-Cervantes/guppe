"""Listas Aninhadas - Nested Lists"""

'''
- Algumas linguagens de programação (C/java)pussuem umas estruturas de dados chamadas de arrays:
  * Unidimensionais (Arrays/Vetores)
  * Bidimensionais (Matrizes)
- Em Python temos as Listas.
  Exemplo:
  numeros = [1, 'b', 3.324, True, 5]
'''

# Exemplos 1:
listas = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
# print(listas)
# print(type(listas))

# Como acessar aos dados
# print(listas[0][2])  # 2
# print(listas[2][1])  # 8

# Iterando com loops uma lista aninhadas
# Impirmindo cada elemento
# for lista in listas:
    # print(lista)

# Imprimindo cada elemento de cada elemento
# for lista in listas:
#     for num in lista:
        # print(num)

# Utilizando List Comprehensions
# [[print(num) for num in lista] for lista in listas]

# Outros Exemplos
# Gerando um tabukeiro (matriz) 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
# print(tabuleiro)

# Gerando jogadas para jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
# print(velha)

# Gerando valores iniciais
# print([['*' for i in range(1, 4)] for j in range(1, 4)])

print('Olá você está no arquivo Listas Aninhadas')