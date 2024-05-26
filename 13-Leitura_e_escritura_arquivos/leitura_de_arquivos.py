"""Leitura de arquivos"""
'''
- Não inetersa o tamanho do arquivo.
- Para o conteudo de um arquivo em python, utilizamos a função integrada open(), que literalmente significa 'Abrir'
- open() --> Na forma mais simples de utilização nós passamos apenas um parâmetro de entreda, que nesse caso é o 
caminho do arquivo a ser lido. Essa função retorna um '_io'. TextIOWrapper e é com ele que trabalhamos então.   
- Para maiores informações: https://docs.python.org/3/library/functions.html#open
- OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro
'FileNotFoundError 
'''
# Exemplo 1: Abertura de uma arquivo - open()
arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))
'''- <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>
OBS:- mode='r' -> Modo leitura -> r = read (ler)'''


# Exemplo 2: Para ler o conteudo de um arquivo, apos sua abertura, devemos usar a função read()
# Mas antes vou criar uma variavel 'ret' de retorno para saber que tipo de rerorno nos envia a função read()

ret = arquivo.read()
# print(type(ret))
# print(ret)

# print(arquivo.read())
'''Eu estou estudando na Geek University e estou aprendendo muito no curso de programaÃ§Ã£o em Python: Essencial'''

# OBS: Python trabalha com um recurso para trabalhar com arquivos chamados 'CURSOR'. Esse 'CURSOR' funciona como o
# cursor quando estamos escrevendo.

# print(arquivo.read())
# OBS: A função read() lé thodo o conteudo do arquivo. Não funciona o cursor.

print('Olá vc esta no arquivo leitura de arquivos')


