from random import randint as rd
"""O 'ELSE' nos possibilita executar um bloco de código após a condição ter sido satisfeita. Porém, o 'ELSE' não é 
executado quando o 'WHILE' encontra uma cláusula 'BREAK! Vamos entender melhor no exemplo:"""

numero_magico = rd(0,10)
tentativas = 0

while tentativas < 3:
    numero = input('Adivinhe o número mágico (0 a 10): ')

    if int(numero) == numero_magico:
        print('Corre pra Loteria! Hoje é seu dia de sorte *.*')
        break
    tentativas += 1
else:
    print('Teeeente outra veeeez xD')