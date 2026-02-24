"""
PEP8 - Python Enhancement Proposals
São propostas de melhoria para a linguagem Python
import this
A ideia da PEP8 é que possamos escrever código de forma Pythonica.

[1] - Utilize Camel Case para nomes de Classes:
class CamelCase:
    pass
class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções o variáveis
def soma():
    pass
def soma_dois():
    pass
numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para indentação (não use TAB)
if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- separar funções e declarações de classe com duas linhas em branco.
- Métodos numa classe deven ser separados com uma unica linha em branco.

[5] - Imports
- Imports debem ser feitos em linhas separadas;
# import errado
import sys, os

# import certo
import sys
import os
from ctypes import SetPointerType

# Não tem problema em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacotes, recomenda-se fazer:
from types import {
    StringType
    ListType
    SetType
    OutroType
}

# Imports debem ser colocados no topo do arquivo, logo depois de quaisquer comentário ou docstring e antes de constates
# ou variáveis globais.
[6] - Espaços em expressões e instruções
# Não faça:
funcao( algo[ 1 ], { outro: 2 } )

# Faça:
funcao(algo[1], {outro:2})

# Não faça
algo (1)

# Faça:
algo(1)

# Não faça:
dict ['chave'] = lista [indice]
# Faça:
dict['chave'] = lista[indice]

# Não faça:
x               = 1
y               = 3
variavel_longa  = 5

# Faça:
x = 1
y = 3
variavel_longa  = 5

[7] - Termine sempre uma instrução em uma linha em branco
"""










