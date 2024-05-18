"""Seek e Cursor"""

'''
seek() --> É utilizada para mover o cusor pelo arquivo. Ela revece um parametro onde indica onde queremos colocar o 
cursor  

'''
arquivo = open('texto.txt', encoding='UTF-8')

# print(arquivo.read())

# Movivmentando o cursor com a função seek()
# arquivo.seek(0) # O cursor estara apartir do carater 0, ou seja, antes do texto inicira. Então mostrara tudo o texto
# desee o inixio

# print(arquivo.read())

# arquivo.seek(22) # O cursor estara apartir do carater 22, e ai ele cai imprimir.
# print(arquivo.read())

'''readline() -> Função que lê o arquivo linha a linha'''
# print(arquivo.readline())  # Imprime a 1 linha
# print(arquivo.readline())  # Imprime a 2 linha
# print(arquivo.readline())  # Imprime a 3 linha
# print(arquivo.readline())  # Imprime a 4 linha
# print(arquivo.readline())  # Imprime a 5 linha
# print(arquivo.readline())  # Imprime a 6 linha
# print(arquivo.readline())  # Imprime a 7 linha
# print(arquivo.readline())  # Imprime a 8 linha

'''Vamos ver o retorno'''
# ret = arquivo.readline()
# print(type(ret))
# print(ret)
# print(ret.split(' '))

'''As veces vc vai querer fazer a leitura mas transformar em umas lista - readlines()'''
# print(arquivo.readlines())

'''Se queremos saber o numeros de linhas podemos usar - len'''
# linhas = arquivo.readlines()
# print(len(linhas))

'''OBS: Quando abrimos um arquivo com a função open(), se cria uma conexão entre seu computador e nosso programa. Essa
conexão é chamada de 'streaming'. Ao finalizar nossos trabalhos devemos fechar essa conexão com a função close()'''

# Passos para trabalhar com um arquvo

# 1) Abrir um arquivo
'''arquivo = open('texto.txt')'''
# 2) Trabalhar um arquivo
'''print(arquivo.read())'''
# Verificar se o arquivo esta aberto ou fechado
'''print(arquivo.closed()) - Nesse nivel a saida é FALSE, porque o arquivo esta aberto ainda'''
# 3) Fechar um arquivo
'''arquivo.close()'''
# Verificar se o arquivo esta aberto ou fechado
'''print(arquivo.closed()) - Nesse nivel a saida é TRUE, porque o arquivo esta fechado já'''
# Se tentarmos manipular um arquivo que esta fechado acusará um "ValueError - I/O Operations on closed file"
'''Com a função read() podemos limitar a quantidade de carateres a seren lidos no arquivo'''
# print(arquivo.read(50))

print('Olá vc está no arquivo seek e cursor')
