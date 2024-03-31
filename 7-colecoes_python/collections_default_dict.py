from collections import defaultdict
'''https://docs.python.org/3/library/collections.html#collections.defaultdict'''

"""Modulo Collections - Deafult Dict"""
'''
Default Dict: Ao criar um dicionario utilizando-o, nós informamos um valor default podendo utilizar um lambda paera isso
Este valor sempre sera utilizado quando não houver um valor definido. Caso tentemos acessar uma chave que não existe, 
essa chave sera criada e o valor default será atribuido.
OBS: lambda: são funções sem nome, que podem ou não receber parametros de entrada e retornar valores
'''
# Fazendo o import (from collections import defaultdict)
dicionario = defaultdict(lambda: 0)
# print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'
# print(dicionario)

# print(dicionario['outro'])  # Key Error no dicionario comum mas aqui não
# print(dicionario)

print('Olá você esta no arquivo Collections - defaultdict')