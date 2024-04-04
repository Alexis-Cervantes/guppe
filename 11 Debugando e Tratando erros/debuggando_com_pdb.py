import pdb
"""Debuggando com PDB"""

'''
- PDB -> Python Debugger
- Vida de inseto -> Life´s Bug
- Bug -> Inseto

'''
# Exemplo 1: A prática de utilizar o print para debbugar nosso codigo é uma pratica ruim. A forma mais profissional é
# utilizando um debugger nas diferentes IDE´s


# def dividir(a, b):
#     print(f'a = {a}, b = {b}')  # Uma maneira de ver os valores que a função esta processando
#     try:
#         return int(a) / int(b)
#     except (ValueError, ZeroDivisionError):
#         return 'Valor incorreto'


# print(dividir(4, 7))

# Exemplo 2: Utillizando Pycharm


# def dividir(a, b):
#     try:
#         return int(a) / int(b)
#     except (ValueError, ZeroDivisionError):
#         return 'Valor incorreto'
#
#
# print(dividir(4, 7))

# Exemplo 3: Utillizando PDB - Python Debbuger:
# Primeiro precisamos importar a biblioteca 'pdb'
# Utilizar a função 'set_trace()'
'''Comandos Básicos do PDB:
    l (Listar onde estamos no código)
    n (próxima linha)
    p (imprime variável)
    c (continua a execução - finaliza o debbuging)
'''
# nome = 'Alexis'
# sobrenome = 'Cervantes'
# pdb.set_trace()
# nome_completo = nome + ' ' + sobrenome
# curso = 'Programação em Python: Essencial'
# final = nome_completo + ' faz o curso' + curso
# print(final)

# Exemplo 4: Outra forma de Utillizar o PDB - Python Debbuger:
# Utilizar o importe do pdb e 'set_trace()' em uma mesma linah

nome = 'Alexis'
sobrenome = 'Cervantes'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso' + curso
print(final)

'''
- Porque utilizar esse formato?
- O debbug é utilizado durante o desenvolvimento. costumamos realizar todos os imports de bibliotecas no inicio do 
arquivo. 
- Por isso, ao invés de colocarmos o import do pdb ao inicio do arquivo, nos colocamos somente no codigo que vvamos 
debbugar. E ao finalzar já fazemos a remoção.
- A partir do Python 3.7 não é mais necessario importar a biblioteca pdb porque o comando 'debgug' foi incorporado a
como função built-in (integrada) chamada de "breakpoint"
'''
