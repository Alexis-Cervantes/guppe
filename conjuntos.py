"""Conjuntos"""

"""
- Conjuntos, em qualquer linguajem de programação, estamos fazendo referencia a teoria dos conjuntos da matematica
- Aqui em Pythom os Conjuntos saõ chamados de SETs
- Dito isso:
    * Sets (conjuntos) não possuem valores duplicados
    * Sets (Conjuntos) não possuem valores ordenados
    * Elementos não são acessados via INDICE. isto é, Conjuntos não são INDEXADOS
- CONJUNTOS SERVEM PARA QUE?
    * São bons quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. 
    * Quando não precisamos se preocupar com CHAVE, VALOR e ITENS duplicados.
    * Sets são referenciados por parentesis {}.
- DIFERENÇA ENTRE CONJUNTOS (SETs) e MAPAS (Dicionario) em Python:
    * Um dicionario tem CHAVE/VALOR.
    * Um conjunto tem apenas VALOR
"""
"""DEFININDO UM CONJUNTO"""
# FORMA 1:
# repare que temos valores repeptidos:
s1 = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
# print(s1)
# print(type(s1))
# OBS: So mostra os valores que não se repetem, sem gerar erro.

# FORMA 2: MAS COMUM
s2 = {1, 2, 3, 4, 5, 5}
# print(s2)
# print(type(s2))

# VERIFICAR SE DETERMINADO ELEMENTO ESTA CONTIDO EM UM CONJUNTO
s3 = {1, 2, 3, 4, 5, 5}
# if 3 in s3:
#     print("Encontrei 3")
# else:
#     print("Não encontrei o 3")

# NÃO IMPORTA VALORES REPETIDOS E NEM A ORDEM DELES:
"""LISTAS ACEITAN VALORES DUPLICADAS - 10 elementos"""
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
# print(f"Lista: {lista} com {len(lista)} elementos")

"""TUPLAS ACEITAN VALORES DUPLICADAS - 10 elementos"""
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
# print(f"Tupla: {tupla} com {len(tupla)} elementos")

"""DICIONARIOS NÃO ACEITAM CHAVES DUPLICADAS - 08 elementos"""
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], "dict")
# print(f"Dicionario: {dicionario} com {len(dicionario)} elementos")

"""CONJUNTOS NÃO ACEITAN VALORES DUPLICADAS - 08 elementos"""
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
# print(f"Conjunto: {conjunto} com {len(conjunto)} elementos")

# Podemos colocar qualquer tipos de dados misturados em SET´s
s4 = {1, "b", True, 34.22, 44}
# print(s4)
# print(type(s4))

# Podemos iterar:
# for valor in s4:
#     print(valor)

# Usos interesantes com SET´s
# Formulario de cadastro de visitas: Informam nome de cidade onde eles vem
# cidades iram em LISTA - Aceita repetições

cidades = [
    "Belo Horizonte",
    "São Paulo",
    "Campo Grande",
    "Cuiaba",
    "Campo Grande",
    "São Paulo",
    "Cuiaba",
]
# print(cidades)
# print(len(cidades))

# Agora devemos saber quantas cidades unicas temos. SEM SE REPETIR
# Fazer um LOOP na lista usando SET´s. Isso filtra so cidades sem repetição
# print(len(set(cidades)))

'''Adicionando elementos a Conjuntos'''
s5 = {1, 2, 3}

# add
# s5.add(4)
# s5.add(4)  # Duplidade não gera erro. Simplesmente é ignorado e não adicionado
# print(s5)

# remove - remover elementos
s6 = {1, 2, 3}
# print(s6)

# Forma 1:

# s6.remove(3)  # Não é indice. Informamos o valor a ser removidos
# print(s6)  # Nehum valor é retornado
# s6.remove(33)  # Caso valor não fosse encontrado. Gera Erro
# print(s6)

# Forma 2:
s7 = {1, 2, 3}
# print(s7)

# discad # remove valores
# s7.discard(2)
# print(s7)
# 
# s7.discard(22)  # Se valor não é encontrado não gera nehum erro
# print(s7)

'''Copiando um cojunto para outro'''
s8 = {1, 2, 3}
# print(s8)

# Forma 1: Deep Copy
# novo_s8 = s8.copy()
# print(novo_s8)
#
# novo_s8.add(4)
#
# print(novo_s8)
# print(s8)

# Forma 2: Shallow Copy
# novo_s8 = s8  # Estas duas variaveis vão ter os mesmos valores
#
# novo_s8.add(4)
#
# print(novo_s8)
# print(s8)

'''Podemos remover elementos de um conjunto'''
# s8.clear()
# print(s8)

'''Metodos matematicos de conjuntos
primer conjunto: Alunos estudantes de Python
segunod conjunto: alunos estudantes de Java'''

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', "Julia", 'Gilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
# Alguns alunos que estudam Python tambem estudan java
# Temos que gerar conjuntos com nomes de estudasntes unicos

# Forma 1 - UNION - MAS RECOMENDADO
unicos1 = estudantes_python.union(estudantes_java)
unicos2 = estudantes_java.union(estudantes_python)
# print(unicos1)
# print(unicos2)

# Forma 2 - carater pape '|'
unicos3 = estudantes_python | estudantes_java
# print(unicos3)

# Gerar conjunto de estudantes que estão em ambos os cursos
# Forma 1 - Intersection
ambos1 = estudantes_python.intersection(estudantes_java)
# print(ambos1)

# Forma 2 - Utilizando '&'
ambos2 = estudantes_python & estudantes_java
# print(ambos2)

# Gerar conjunto estudasntes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
# print(so_python)

so_java = estudantes_java.difference(estudantes_python)
# print(so_java)

# Soma, Valor max, Valor min, Tamanho - Se os valores foram inteiros e reais
s9 = {1, 2, 3, 4, 5, 6}
# print(sum(s9))
# print(max(s9))
# print(min(s9))
# print(len(s9))

print('Olá, você esta no Arquivo Conjuntos')


