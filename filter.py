import statistics
"""Filter()"""
'''
- Serve para filtrar dados de uma determnada coleção
- Recebe 02 parametros: A primeira (FUNÇÃO) e a Segunda (ITERAVEL)
- DIFERENÇA: 
  * Map(): receve 02 parametros (Função e Iteravel) e retorna 01 objeto mapeando a função para cada elemento do iteravel.   
  * Filter(): receve 02 parametros (Função e Iteravel) e retorna 01 objeto filtranado apenas os elementos de acordo com
  a função 
'''
# Exemplo 1: Digamos que queremos saber a media de valores de uma tupla
valores = 1, 2, 3, 4, 5, 6

media1 = sum(valores) / len(valores)
# print(media1)

# Exemplo 2:
# 'Import estaitstic': biblioteca que trabalaha com dados estatisticos

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media2 = statistics.mean(dados)
# print(f'A media de dados é {media2}')

# Exemplo 3: Utilizando FILTER
# Filter recebe 02 parametros: função lambda e Iteravel dados. A função va pegar cada um dos valores de 'DADOS'.
# E retornará os valores que sejam maior que o valor da media2
res1 = filter(lambda x: x > media2, dados)
# print(type(res1))
# print(list(res1))

'''OBS:Assim como na função map(), apos serem utilizados os dados de filter() foi utiLIzados eles são excluodos da 
memoria'''
# print(f'Novamente {list(res)}')

'''DADOS FALTANTES'''
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# print(f'paises sem filter: {paises}')

res2 = filter(None, paises)  # None elimina espaçoes em branco
print(f'paises com filter {list(res2)}')

# Outro modo de fazer a mesma coisa que o FILTER utilizando LAMBDA 01
res3 = filter(lambda pais: len(pais) > 0, paises)
print(f'paises utlizando função lambda v1: {list(res3)}')

# Outro modo de fazer a mesma coisa que o FILTER utilizando LAMBDA 02
res4 = filter(lambda pais: pais != '', paises)
print(f'paises utlizando função lambda v2: {list(res4)}')