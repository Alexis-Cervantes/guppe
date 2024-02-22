"""Dicionarios - 1era Parte"""

"""OBS: Em alguns linguagens de programação os diccionarios de Python são conhecidos por Mapas
Dicionarios são coleccines de tipo chave/valor
Diccionarios são representado por {}
obs: sobre dicionarios
    - Chave e valor são separados por dois pontos  "chave: valor";
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;"""
# print(type({}))

"""CRIAÇÃO DE DICIONARIOS"""
# Forma 1 (mais comum)
# paises1 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# print(paises1)
# print(type(paises1))

# Forma 2 (menos comum)
# paises2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
# print(paises2)
# print(type(paises2))

"""ACESSANDO ELEMENTOS"""
# paises3 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Forma 1: Acessando via chave, do mesmo jeito que lista/tupla
# print(paises3['br'])
# print(paises3['ru'])
# OBS: Quando inserimos um dado inesistente. Da erro - KeyError

# Forma 2: Acessando via "get" - Recomendada
# print(paises3.get('br'))
# OBS: Quando inserimos um dado inesistente. Mostra None. E não sera gerado KeyError
# print(paises3.get('ru'))


"""ACESSANDO COM GET - recomendado"""
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

paises6 = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}
# pais = paises6.get('ru', 'Não encontrado')
# print(f'Encontreo pais {pais}')
# Podemos definir um valor padrão para caso no encontremops o objeto com a chave informada

"""VERIFICANDO SE DETERMINADO CHAVE ESTA DENTRO DE UM DICIONARIO"""
paises7 = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}
# print('br' in paises7)
# print('ru' in paises7)
# print('Estados Unidos' in paises7)
#
# if 'ru' in paises7:
#     russia = paises7['ru']
"""Podemos utilizar qualquet tipo de dado:  int, float, string, boolean, listas, tuplas, diccionario - com chaves de di
cionario
Tuplas: são interessantes de ser utilizadas como chave de dicionario porque são IMUTAVEIS"""
# localidades = {
#     (35.6895, 39.6917): 'Escritorio em Tokio',
#     (40.7128, 74.0060): 'Escritorio em Nova York',
#     (37.7749, 122.4194): 'Escritorio em São Paulo',
# }
# print(localidades)
# print(type(localidades))

"""ADICIONAR ELEMENTOS EM UM DICCIONARIO"""
receita = {"jan": 100, "fev": 120, "mar": 300}

# print(receita)
# print(type(receita))

# Forma 1: MAIS COMUM
# receita['abr'] = 350
# print(receita)

# Forma 2:
# novo_dado = {'mai': 500}
# receita.update(novo_dado)  # ou receita.update({'mai'}: 500)
# print(receita)

"""ATUALIZANDO DADOS EM UM DICIONARIO"""
# Forma 1:
# receita['mai'] = 550
# print(receita)

# Forma 2:
# receita.update({'mai': 600})
# print(receita)

"""OBS:
1. A forma de adicionar novos elementos ou atualizar dados em um dicionarios é a mesma
2. Em dicionarios NÃO podemos ter chaves repetidas"""

"""REMOVER DADOS"""
receita2 = {"jan": 100, "fev": 120, "mar": 300}
# print(receita2)

# Forma 1: mais comum
# Presisamos informar a chave obrigatoriamente.
# Em caso de não encontrar o elemento um KeyError é retornado.
# ret = receita2.pop('mar')
# print(ret)
# print(receita2)

# Forma 2:
# Neste caso o valor removido não é retornado
# del receita2['fev']
# print(receita2)

"""e-commerce:
Carrinho de compras: vamos adicionar produtos
CARRINHO DE COMPRAS:
    Produto 1 :
    - nome;
    - quantidade;
    - preço;
    Produto 2 :
    - nome;
    - quantidade;
    - preço;
"""
# 1. Poderiamos usar uma lista para isso
# carrinho1 = []
#
# produto1 = ['PlaySatation 4', 1, 2300.00]
# produto2 = ['God of war 4', 1, 150.00]
#
# carrinho1.append(produto1)
# carrinho1.append(produto2)
#
# print(carrinho1)
# OBS: Teriamos que saber qual é o indice de informação no produto

# 2. Poderiamos utilizar uma tupla
# produto3 = ('PlaySatation 4', 1, 2300.00)
# produto4 = ('God of war 4', 1, 150.00)
#
# carrinho2 = (produto3, produto4)
#
# print(carrinho2)
# OBS: Teriamos que saber qual é o indice de informação no produto

# 3. Poderiamos utilizar um dicionario
# carrinho3 = []
#
# produto1 = {'nome': 'PlaySatation 4', 'quanttidade': 1, 'preco': 2300.00, }
# produto2 = {'nome': 'God of war 4', 'quantiadde': 1, 'preco': 150.00}
#
# carrinho3.append(produto1)
# carrinho3.append(produto2)
#
# print(carrinho3)
# OBS: Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter certeza sobre
# cada informação

"""METODOS DE DICIONARIOS"""
d1 = dict(a=1, b=2, c=3)
# print(d1)
# print(type(d1))

# LIMPAR DICIONARIOS (ZERAR DADOS) .clear()
# d1.clear()
# print(d1)

# COPIANDO UM DICIONARIO PARA OTRO - .copy()
d2 = dict(a=1, b=2, c=3)

# Forma 1:  Deep Copy
# novo_d2 = d2.copy()
# print(novo_d2)
#
# novo_d2['d'] = 4
#
# print(d2)
# print(novo_d2)

# Forma 2:  Shallow Copy
d3 = dict(a=1, b=2, c=3)

# novo_d3 = d3
# print(novo_d3)
#
# novo_d3['d'] = 4
#
# print(d3)
# print(novo_d3)

"""FORMA NÃO USUAAL DE CRIAR DICIONARIOSO"""
outro = {}.fromkeys("a", "b")
# print(outro)
# print(type(outro))

# usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
# print(usuario)
# print(type(usuario))
"""O metodo fromkeys: receve 2 parametros: 01 iteravel e 01 valor
Ele vai gerar para cada valor do iteravel 01 chave e ira a atribuir a essa chave o valor informado"""

veja1 = {}.fromkeys("teste", "valor")  # Aqui não repete chaves. So mostra t, e, s
# print(veja1)
#
# veja2 = {}.fromkeys(range(1, 11), 'novo')
# print(veja2)

print("Olá, vc esta no arquivo Dicionarios")
