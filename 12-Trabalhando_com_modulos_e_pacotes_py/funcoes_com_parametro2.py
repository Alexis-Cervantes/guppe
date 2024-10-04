"""Funções com parametro - Entrada - Aquivo duplicado para praticar com o arquivo modulos customizados"""

# Exemplo 1: Usando uma função quanquer:


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

# Funções:


def soma(a, b):
    return a + b


# print(soma(2, 5))
# print(soma(10, 20))


def multiplica(num1, num2):
    return num1 * num2


# print(multiplica(4, 5))
# print(multiplica(2, 8))


def outra(num1, b, msg):
    return (num1 + b) * msg


# print(outra(3, 2, 'Alexis'))
# print(outra(5, 4, 'Cervantes'))


# Funções como parametro nomeados


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


# print(nome_completo('Alexis', 'Cervantes'))

# A ordem dos parametros importam
nome = 'Juan'
sobrenome = 'Aguirre'

# print(nome_completo(sobrenome, nome))


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        # return total -> Se coloccamos o return nessa posição vai encerrar logo a função
    return total  # Posição certo do return


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))



