"""Modos de Abertura"""
'''
r = abre para leitura (padr�o).
w = abre para escrita (sobrescreve caso arquivo exista).
x = abre para escrita somente si o arquivo n�o existir. Caso o arquivo exista gera (fileExistErro).
a = abre para escrita, adicionando o conteudo ao final do arquivo.
+ = abre pro modo atualização: leitura e escrita.
OBS: abriendo no modo 'a' -> append. Se o arquivo não existir sera criado. Caso exista o novo conteudo sera adicionado
ao final
https://docs.python.org/3/library/functions.html#open
'''

# 1er. Caso de uso: Arquivo não existe e ele va criar. Se Rdamos de novo var dar erro porque o arquivo ja existe
# with open('ntm.txt', 'x') as arquivo:
#     arquivo.write('teste de conteudo\n')

# 2do. Caso de uso: Arquivo foi criado e agora podemos reescrever
# with open('ntm.txt', 'w') as arquivo:
#     arquivo.write('teste de conteudo\n')

# 3ro. Caso de uso: Arquivo criado e rodamos de novo. Para evitar essa mensagen feia podemos usar Try/except
# try:
#     with open('ntm.txt', 'x') as arquivo:
#         arquivo.write('teste de conteudo\n')
# except FileExistsError:
#     print('Arquivo ja existe')

# 4to Caso de uso: Modificando nu arquivo existente
# Primeiro vamos criar nosso arquivo:
# with open('frutitas.txt', 'x') as arquivo:
#     arquivo.write('banana, morango, uva\n')

# 4to Caso de uso: Modificando nu arquivo existente
# Vamos agora modificar o arquivo frutitas usando o 'w':
# with open('frutitas.txt', 'w') as arquivo:
#     while True:
#         frutitas = input('Informa uma fruta ao sair: ')
#         if frutitas != 'sair':
#             arquivo.write(frutitas)
#             arquivo.write('\n')
#         else:
#             break

# # 5to Caso de uso: Usando modo 'a'. Adicionando conteudo no final do texto existente
# with open('frutitas.txt', 'a') as arquivo:
#     while True:
#         frutitas = input('Informa uma fruta ao sair: ')
#         if frutitas != 'sair':
#             arquivo.write(frutitas)
#             arquivo.write('\n')
#         else:
#             break

# # 6to Caso de uso: Usando modo 'a'. Adicionando conteudo no inicio do texto existente com curso seek
# with open('frutitas.txt', 'a') as arquivo:
#     arquivo.seek(0) #O curso não modifica posição. Se reescreve ao final
#     arquivo.write('Linha1 no topo usando modo a\n')
#     arquivo.write('Linha2 no topo usando modo a\n')
#     arquivo.write('Linha3 no topo usando modo a\n')

# 7mo Caso de uso: Usando modo 'a+'. Adicionando conteudo no inicio do texto existente com curso seek
# with open('frutitas.txt', 'a+') as arquivo:
#     arquivo.write('de novo Linha3 no topo usando modo a+\n')
#     arquivo.write('de novo Linha4 no topo usando modo a+\n')
#     arquivo.write('de novo Linha5 no topo usando modo a+\n')

print('Estas no Modos de abertura de arquivos')



