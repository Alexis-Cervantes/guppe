"""Funções com parametro - Entrada"""
'''Funções que recebem dados para serem procesados dentro da mesma
Exemplo: ENTRADA -> PROCESSAMENTO -> SAIDA
FUNÇÕES: Tem as que não possuem entrada (Somente executam algo); 
         Não possuem saida;
         Possuem entrada mas não possuem saida;
         Não possuem entrada mas possuem saida;
         Possuem entrada e possuem saida;'''

# Refaturando uma função:


# Exemplo 1: Usando uma função quanquer.
def quadrado_de_7():
    return 7 * 7


# print(quadrado_de_7())  # Comportamento esperado.
# print(quadrado_de_7())  # Comportamento esperado.
# print(quadrado_de_7())  # Comportamento esperado.

# Refatorando:


def quadrado(numero):
#  return numero * numero
    return numero ** 2


# print(quadrado(7))
# print(quadrado(2))
# print(quadrado(5))
# print(quadrado())  # Type Error

# Refatorando a função:


def cantando_parabens1():
    print('Parabens pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o anirversariante!')


# print(cantando_parabens1())

# Refatorando:


def cantando_parabens2(aniversariante):
    print('Parabens pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')


# print(cantando_parabens2('Alexis'))

'''OBS: Funçoes podem ter n parametros de entrada. Ou seja podemos receber como parâmetros de entrada quantos foram
necessários. Eles são separados por virgola'''

# Exemplo 1:


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


# print(soma(2, 5))
# print(soma(10, 20))

# print(multiplica(4, 5))
# print(multiplica(2, 8))

# print(outra(3, 2, 'Alexis'))
# print(outra(5, 4, 'Cervantes'))


'''OBS: Se erramos de informar um numero errado de parametros ou argumentos. Teremos TypeError'''

# NOMEANDO PARAMETROS


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


# print(nome_completo('Alexis', 'Cervantes'))

'''OBS: Diferença entre Pararametros e Argumentos
- PARAMETROS: Variaveis declaradas na definição de uma função
- ARGUMENTOS: Dados passados durante a execução de uma função
'''
# A ordem dos parametros importam
nome = 'Juan'
sobrenome = 'Aguirre'
# print(nome_completo(sobrenome, nome))

'''ARGUMENTOS NOMEADOS - Keyword Arguments: Caso Utilizemos nomes dos parametros nos argumentos para informá-los, 
podemos utilizar qualquer ordem'''
# Exemplo:
# print(nome_completo(nome='Alexxis', sobrenome='Cervantes'))
# print(nome_completo(nome=nome, sobrenome=sobrenome))
# print(nome_completo(sobrenome='Marques', nome='Marcia'))

# Erro muito comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
      # return total -> Se coloccamos o return nessa posição vai encerrar logo a função
    return total  # Posição certo do return


lista = [1, 2, 3, 4, 5, 6, 7]
# print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
# print(soma_impares(tupla))

print('Ola, estamos no arquivo Funções com Parametros')


