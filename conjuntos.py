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
s1 = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
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
print(cidades)
print(len(cidades))
# Agora devemos saber quantas cidades unicas temos
# fazer um LOOP na lista usando SET´s
print(len(set(cidades)))
