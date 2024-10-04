"""MAPAS - dicionario - 2da parte"""

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
# print(receita2)

# Acessando as Chaves 1:
# print(receita2.keys())

# Acessando as Chaves 2 - Combinando com for - Para saber os valores - Modo Pythonico
# for chave in receita2.keys():
#     print(receita2[chave])

# Acessando os Valores: Modo Pythonico
# print(receita2.values())
# for valor in receita2.values():
#     print(valor)

"""Desempacotamento de dicionarios"""
receita3 = {"jan": 100, "fev": 120, "mar": 300}
# print(receita3.items())
#
# for chave, valor in receita3.items():
#     print(f"chave={chave} e valor={valor}")

"""Soma, valor max, valor mim, tamanho"""
receita4 = {"jan": 100, "fev": 120, "mar": 300}

# OBS: Funciona se os elementos são inteiros e reais
# print(sum(receita4.values()))
# print(max(receita4.values()))
# print(min(receita4.values()))
# print(len(receita4))

print("Olá, vc esta no arquivo Mapas - 2da parte de dicionarios")
