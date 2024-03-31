"""Funções com parametro Padrão - Default Parameters"""

'''Funções onde a passagem de parametro seja OPCIONAL - Não da erro'''
# print('Alexis Cervantes')  # Passo parametro
# print()  # Não passo parametro

'''Funções onde a passagem de parametro seja OBRIGATORIA - Da erro'''


def quadrado(numero):
    return numero ** 2


# print(quadrado(3))  # imprimiu 9 no console
# print(quadrado())  # TypeError


def exponencial1(numero, expoente):
    return numero ** expoente


# print(exponencial1(2, 3))
# print(exponencial1(3, 2))

'''REFATORANDO FUNÇÃO ANTERIOR'''
# Como fazer para que o parametro "expoente" na função exponencial seja "2 - ao quadrado" por PADRÃO

# Exemplo 1:  # Nesta função o Parametro 'numero=2' fica como opcional. Em caso que não esteja definido um valor
# opcional a chamada acarretara um erro
def exponencial2(numero, expoente=2):
    return numero ** expoente


# print(exponencial2(3))  # Se passamos um argumento, este sera atribuido ao parametro 'numero' e sera calculado o quadra-
# do desse nume;
# print(exponencial2(3, 5))  # Se passamos 2 argumentos o 1ro sera atribuido ao parametreo 'numero' e o
# segudo ao parametro 'potencia'. Então sera calculada essa potencia

# Exemplo 2: E se querenos que os dois valores (parametros: numero e expoente) fiquem opcionais
def exponencial3(numero=4, expoente=2):  # Parametro numero e expoente ficam como opcionais
    return numero ** expoente


# print(exponencial3(3))  # Se passamos 1 argumento: Este sera atribuido o primer argumento. Ao parametro 'numero=4', e
# diante a falta do segundo argumento (expoente) entrará em cena o valor OPCIONAL (expoente=2) calculado o quadrado
# desse numero;
# print(exponencial3(3, 5))  # Se passamos 2 argumentos: Os dois se irão impor aos parametros OPCIONAIS.
# O argumento '3' ao parametro 'numero=4', e o argumento '5' ao parametro 'expoente=2'. Então sera calculado a raiz
# quinta do numero.
# print(exponencial3())  # Aqui tambem vai funcionar normalmente. Porque so dois PARAMETROS OPCIONAIS entrão em cena

'''OBS: Em Python, os parametros default (padrão) SEMPRE tem que estar no final da declaração'''
# Exemplo 1: ERRO
# def teste1(num=2, exp):  # Não podemos declarar um parametro DEFAULT na 1ra posição e NADA no segundo parametro
#     return num ** exp


# print(teste1(6)) # SyntaxError: parameter without a default follows parameter with a default

# Exemplo 1: CERTO
def teste2(exp, num=2):  # Não podemos declarar um parametro DEFAULT na 1ra posição e NADA no segundo parametro
    return num ** exp


# print(teste2(6)) # SyntaxError: parameter without a default follows parameter with a default


'''OUTROS EXEMPLOS'''


def soma1(num1, num2):
    return num1 + num2


# print(soma1(4, 3))  # CERTO
# print(soma1(4))  # TypeError: soma() missing 1 required positional argument: 'num2'
# print(soma1())  # TypeError

# PARA CORREGIR ISSO DEVEMOS COLOCAR VALORES AOS PARAMETROS (DEFAULT)
def soma2(num1=5, num2=3):
    return num1 + num2


# print(soma2(4, 3))  # CERTO
# print(soma2(4))
# print(soma2())

'''EXEMPLO MAIS COMPLEXO'''

def mostra_informacao(nome='Alexis', instrutor=False):
    if nome == 'Alexis' and instrutor:  # and instrutor==True
        return 'Bem-vindo instrutor Alexis'
    elif nome == 'Alexis':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


# print(mostra_informacao())
# print(mostra_informacao(instrutor=True))
# print(mostra_informacao(True))
# print(mostra_informacao('Ozzy'))
# print(mostra_informacao('Stephany'))

'''
POR QUE UTILIZAR PARAMETROS COM VALORES DEFAULT
- Nos permite ser mais flexiveis nas funções
- Evita erros com parametros incorretos
- Nos permite trabaalhar com parametros mais legíveis de codigo

QUAIS TIPOS DE DADOS PODEMOS UTILIZAR COMO VALORES DEFAULT PARA PARAMETROS
- Números, Strings, Floats, Booleanos, Listas, Tuplas, Dicionarios, Funções e etc
'''
# Exemplos:


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def substracao(num1, num2):
    return num1 - num2


# print(mat(2, 3))
# print(mat(2, 2, substracao))

'''ESCOPO -> Evitar confuções
- Variáveis Globais ->
- Variáveis Locais ->
'''
# Exemplo 1:
instrutor = 'Alexis'  # variavel GLOBAL


def diz_oi():
    instrutor = 'Python'  # variavel LOCAL com o mesmo nome da GLOBAL. Ela tera preferência
    return f'Oi {instrutor}'


# print(diz_oi())

# Exemplo 2:


def diz_ola():
    prof = 'Alexis'  # Variavel LOCAL
    return f'Olá {prof}'


# print(diz_ola())
# print(prof)  # NameError: name 'prof' is not defined

'''ATENÇÃO: com variaveis GLOBAIS, se puder evitar evite'''
# Exemplo 1: ERRADO
# total = 0

# def incrementa1():
#     total = total + 1  # UnboundLocalError: cannot access local variable 'total' where it is not associated with a
#     value
#     return total
#
# print(incrementa1())

# Exemplo 2: Refatorando a função anterior

total = 0


def incrementa2():
    global total  # AVISAMOS que queremos utilizar a variavel GLOBAL
    total = total + 1
    return total


# print(incrementa2())
# print(incrementa2())
# print(incrementa2())


'''PODEMOS TER FUNÇÕES QUE SÃO DECLARADAS DENTRO DE FUNÇÕES, E TAMBEM TEM UMA ESPECIA DE ESCOPO DE VARIAVEL'''


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Não é uma variavel LOCAL nem GLOBAL. É uma variavel que esta num função anterior

        contador += 1
        return contador
    return dentro()

# print(fora())
# print(fora())
# print(fora())
#
# print(dentro())  #  NameError: name 'dentro' is not defined


print('Ola, você esta dentro do arquivo Funções com parametros Padrão - DEFAULT')

