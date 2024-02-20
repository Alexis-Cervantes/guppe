"""Dicionarios"""
'''OBS: Em alguns linguagens de programação os diccionarios de Python são conhecidos por Mapas
Dicionarios são coleccines de tipo chave/valor
Diccionarios são representado por {}
obs: sobre dicionarios
    - Chave e valor são separados por dois pontos  "chave: valor";
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;'''
# print(type({}))

'''CRIAÇÃO DE DICIONARIOS'''
# Forma 1 (mais comum)
# paises1 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# print(paises1)
# print(type(paises1))

# Forma 2 (menos comum)
# paises2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
# print(paises2)
# print(type(paises2))

'''ACESSANDO ELEMENTOS'''
# paises3 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Forma 1: Acessando via chave, do mesmo jeito que lista/tupla
# print(paises3['br'])
# print(paises3['ru'])
# OBS: Quando inserimos um dado inesistente. Da erro - KeyError

# Forma 2: Acessando via "get" - Recomendada
# print(paises3.get('br'))
# print(paises3.get('ru'))
# OBS: Quando inserimos um dado inesistente. Mostra None

'''ACESSANDO COM GET - recomendado'''
# paises4 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# russia = paises4.get('ru')
#
# if russia:
#     print('Encontrei o pais')
# else:
#     print('Não encointrei o pais')

# paises5 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# pais = paises5.get('py')
#
# if pais:
#     print('Encontrei o pais')
# else:
#     print('Não encointrei o pais')

paises6 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises6.get('ru', 'Não encontrado')
print(f'Encontreo pais {pais}')