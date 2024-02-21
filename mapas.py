"""MAPAS"""

"""Mapas: Conhecidos em paython como dicionarios
Dicionarios são representados por parentesis {}"""

receita1 = {"jan": 100, "fev": 120, "mar": 300}
# print(receita1)
#
# print()
#
# # Iterar sobre dicionarios
# for chave in receita1:
#     print(chave)
#
# print()
#
# for chave in receita1:
#     print(receita1[chave])
#
# print()
#
# for chave in receita1:
#     print(chave, receita1[chave])
#
# print()
#
# for chave in receita1:
#     print(f"Em {chave} recebi R$ {receita1[chave]}")
#
# print()
#
# for item, chave in enumerate(receita1):
#     print(item, chave, receita1[chave])
#
# print()
#
# for item, chave in enumerate(receita1):
#     print(f"item {item} em {chave} recebi R$ {receita1[chave]}")

"""Conhecer as chaves do dicionario - keys"""
receita2 = {"jan": 100, "fev": 120, "mar": 300}
print(receita2)
print(receita2.keys())

# combinado com loop - for
for chave in receita2.keys():
    print(receita2[chave])
