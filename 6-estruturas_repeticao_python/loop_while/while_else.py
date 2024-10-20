# from random import randint as rd
"""O 'ELSE' nos possibilita executar um bloco de código após a condição ter sido satisfeita. Porém, o 'ELSE' não é 
executado quando o 'WHILE' encontra uma cláusula 'BREAK! Vamos entender melhor no exemplo:"""

# numero_magico = rd(0,10)
# tentativas = 0
#
# while tentativas < 3:
#     numero = input('Adivinhe o número mágico (0 a 10): ')
#
#     if int(numero) == numero_magico:
#         print('Corre pra Loteria! Hoje é seu dia de sorte *.*')
#         break
#     tentativas += 1
# else:
#     print('Teeeente outra veeeez xD')

""" WHILE: CRIANDO UM LOOP """
# x = 0
# while x < 10:
#     print(f'O valor de x é: {x}')
#     print('O valor de x é menor que 10, vamos adicionar 1')
#     x += 1

""" WHILE: CONDIÇÕES BOOLEANAS """
# x = 0
# while x < 10:
#     print(f'O valor de x é: {x}')
#     print(f'O valor de x é menor que 10, vamos adicionar mais 1')
#     x += 1

""" WHILE: OPERAÇÕES DE COMPARAÇÃO """
# idade = 0
# while idade <= 18:
#     print(f'Você tem {idade} anos.')
#     idade += 1

""" WHILE: LOOP INFINITO """
# while True:
#     print('este loop nunca terminará')

""" WHILE +  BREAK """
# contador = 0
# while True:
#     print(f'O valor de contador é: {contador}')
#     if contador == 5:
#         print('Break atingido')
#         break
#     contador += 1

""" WHILE +  CONTINUE """
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue
#     print(f'contador impar: {contador}')

""" WHILE +  ELSE """
# contador = 0
# while contador < 5:
#     print(f'valor do contador é: {contador}')
#     contador += 1
# else: print('Loop concluido com sucesso')
# print(f'valor do contador é: {contador}')

""" WHILE ANINHADO """
# externo = 0
# while externo < 3:
#     interno = 0
#     while interno < 3:
#         print(f'ext: {externo}, int: {interno}')
#         interno += 1
#     externo +=1

""" WHILE: VALIDAÇÃO DE ENTREDA DE UM USUARIO """
senha = ''
while len(senha) < 8 or not any(char.isdigit() for char in senha):
    senha = input('senha forte: ')
    print('senha cadastrada com sucesso: ')
