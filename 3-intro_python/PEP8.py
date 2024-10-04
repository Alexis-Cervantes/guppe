"""
PEP8 Python Enchancement Proposal
São propostas de melhorias para a linguagem Python
The zem de python
import this
A ideia da PEP8 é que possamos escrever coodigos Python de forma Pythonica

[1] - Utileze Camel case para nomes de clases.
class Calculadora:
    ...


class CalculadoraCientifica:
    pass

[2] - Utileze nomes em minusculo, seprados por underlines para função ou variaveis.
def soma():
    pass


def soma_dois():
    pass

numero = 4

numero_impar = 5

[3] - Utileze 04 espaços para identação! (Não uso tab)
if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco.
    4.1 Separar funções e definições de clase com 02 linhas em branco
    4.2 Metodos dentro de uma clase deven ser separados com 01 linhas em branco
class Classe:
    pass


class Outra:
    ...

[5] - Imports
      5.1 Imports devem ser sempre feitos em linhas separadas
      Import Errado:
      import sys, os

      Import Certo:
      import sys
      import os

      5.2 Não ha problemas em utilizar:
      from Types import StringType, ListType

      5.3 Caso tenha muitos importes de um mesmo pacote, recomeda-se fazer:
      from Types Import (
            StringType,
            ListType,
            SetType,
            OutroType
      )

      5.4 Imports deven ser colocados no topo do arquivo. Logo depois de qualquer comentario ou docstring e
           antes de constantes e variaveis globais

[6] - Espaços em expresções e instruções:
Não faça:
funcao( algo[ 1 ], { outro: 2})
Faça:
funcao(algo[1], {outro: 2})
Não faça:
algo (1):

Faça:
algo(1):

Não faça:
dict ['chave'] = lista [indice]

faça:
dict['chave'] = lista[indice]

Não faça:
x              = 1
y              = 2
variavel_longa = 5

faça
x = 1
y = 2
variavel_longa = 5

[7] Termine sempre uma instrução com uma nova linha

"""
print('Olá, voce está no arquivo PEP8...')


