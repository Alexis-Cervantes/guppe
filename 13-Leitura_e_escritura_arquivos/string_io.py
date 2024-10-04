"""String IO"""

'''
ATENÇÃO: Para ler ou escrever dados e arquivos do SO o software precisa de permissões:
    - Permisão de leitura: para leer o arquivo.
    - Permisão de escrita: para escrever o arquivo.  
String IO -> Utilizado para ler e criar arquivo em memoria 
'''
# Fazendo o Import do String IO
# from io import StringIO

# mensagem = 'Este é apenas um arquivo normal'

# Podemos criar um arquivo em memoria ja com uma string inserida ou mesmmo vazio para inserirmos textos depois
# arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w') este � quivalente com o que esta acima

# Agora tendo o arquivo, podemos utilizar tudo que j� sabemos.
# print(arquivo.read())

# Escrevendo outros Textos
# arquivo.write('Outro texto')

# Podemos inclusive movimentar os cursor
# arquivo.seek(0)

# print(arquivo.read())

print('Ola, vc esta no arquivo "StringIO" ')
