"""Definindo Dunções"""

"""
- Funções são pequenos partes de codigo que realiza tarefas especificas
- Pode ou não recever entrada de dados e retornar uma saida de dados
- Muito uteis para executar procedimentos similares por repetidas vezes
OBS: Se vc escrever uma função que realiza varias tarefas dentro dela; é bom fazer uma verificação para que a função
seja simplicada. 
Já utilizamos varias funções:
print()
len()
max()
min()
count()
dentre outras
"""
# Exemplo de utilização de funções:
cores = ["verde", "amarelo", "azul", "branco"]

# Utilizando a função integrada (Built-in) do Python 'print'
# print(cores)

nome = "Alexis Cervantes"
# print(nome)

# append() => ele esta dentro de cores
cores.append("roxo")
# print(cores)

# Erro de atributo: 'append se utiliza para trabalhar com elemento de tipo lista
# nome.append("Mais dados...")
# print(nome)

# clear() ; Zera a lista (Depnde da lista). Não recebe parametros
cores.clear()
# print(cores)

"""DRY: Don´t Repeat Yourself - Não repeta vc mesmo - Não repeta seu codigo
Em Python a, forma geral de definir uma função é:

def nome_da_função(parametros_da_entrada)
    bloco da função
ONDE: 
* NOME DA GUNÇÃO: Sempre com letra minuscula, e se for nome composto sempre com underline (SNAKE CASE) 
* PARAMETROS DE ENTRADA: Podem ser opcionais, onde tendo maia de um cada um separado por virgola.
* BLOCO DA FUNÇÃO: Corpo da função ou implementação. É onde o processamento da função acontece. Neste bloco pode ter 
retorno ou não da função
"""
"""DEFININDO A  PRIMEIRA FUNÇÃO"""


def diz_oi():
    print("oi")


"""CHAMADA DA EXECUÇÃO"""
# diz_oi()
# ATENÇÃO: Nunca esqueã de usar o pararetnesis ao executar uma função

"""DEFININDO A SEGUNDA FUNÇÃO"""


def cantar_parabens():
    print("parabens para você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print("Viva o aniversariante")


# cantar_parabens()

# for n in range(5):
#     cantar_parabens()

"""Em python podemos inclusive criar variaveis do tipo de uma função e executar esta função a traves da variavel"""
canta = cantar_parabens
# canta()

print("Olá, voce esta no arquivo Definnindo funções")
