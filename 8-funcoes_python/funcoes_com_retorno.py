from random import random
"""Funções com Retorno"""

"""OBS: Em Pythom unso uma função não retorna nenhum valor o retorno é NONE"""
# Exemplo Função


def quadrado_de_7():
    print(7 * 7)


# quadrado_de_7()  # Vemos que monstra um valor no console.

"""Agora vamos criar uma variavel que recebera o chamado da função: para verificar se a função retorna valor"""


def quadrado_de_8():
    print(8 * 8)


# ret8 = quadrado_de_8()  # Criando variavel
# print(f"retorno: {ret8}")  # Confimamos que a função NÃO RETORNA nada. Só imrpime:

'''Em pyrhon quando uma função não retorna nenhum valor, o retorno é None:
- Refatorando uma função: Reescrvendo uma função
- Vamos refatorando um função parecida à anterior: Em python as funções que retornam valores, devem retronar esse 
valores com a palavra reservada "return".
- Não presisamos nesesariamente criar uma variavel para receber o retorno de uma função. Podemos passar a execução da
função para outra funções.'''


def quadrado_de_9():
    return 9 * 9


ret9 = quadrado_de_9()  # Testando se é verdade que ocorre o antes dito. Criamos uma variavel para recever o retorno
# da função.
# print(f'retorno: {ret9}')
# print(f"retorno: {quadrado_de_9()}")

# Refatorando a função diz_oi:
def diz_oi():
    return 'Oi '


# print(diz_oi())  # Presisamos do 'print' para pegar o valor retornado da função.

def diz_ola():
    print('Olá')

# diz_ola()  # Como na função ja envia um print, somente temos que chamar a função.


# Com a função c/retorno podemos interagir assim:
alguem = 'Alexis!'
# print(diz_oi() + alguem)
# Já com a função sem retorno não podemos intergir melhor
# print(diz_ola() + alguem)  # Erro porque None + str não podem ser concatenados
# Solução:
# diz_ola()
# print(alguem)
'''Paravra reservada RETURN
- Finaliza a função
-  Podemos ter, em uma função,  diferentes returns
- podemos, em uma função, retornar quequer tipo e té mesmo multipels valores
'''
# Exemplo 01: Finaliza a função


def diga_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi'
    print('Estou sendo executado apos o retorno...')


# print(diga_oi())

# exemplo 2: Multiples returns
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

# print(nova_funcao())

# Exemplo 3: Podemos rerornar multiples valores
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()  # desempacotando. Criando vaiaveis
# print(num1, num2, num3, num4)
# Melhor é impriir direito: So que ele mostra ou retorna uma tupla por causa das virgolas
# print(outra_funcao())
# print(type(outra_funcao()))

'''Criando uma função para jogar uma moeda  cara e coroa'''
# from random import random


def jogo_moeda():
    # gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

# print(jogo_moeda())


'''Erros mais comuns na utilização dos Returm´s, que na verdade nem é erro, mais sim codificação desnecessária'''


def eh_impar1():
    numero = 5
    if numero %2 != 0:
        return True
    else:  # Desnecessaria. Por ter somente duas posibilidades
        return False


# print(eh_impar1())


# Melhorando a Função: Menos codigo maior dinamaismo
def eh_impar2():
    numero = 5
    if numero %2 != 0:
        return True
    return False


# print(eh_impar2())

print('Olá, vc esta no arquivo Funções com retorno')