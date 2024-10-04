"""TUPLAS"""
'''Tuplas são muito parecidas as listas
Existem 02 diferenças basicas:
1. As tuplas são representadas por parentesis ()
2. As tuplas são IMUTAVEIS. Isto é ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla'''

# CUIDADO 1: As tuplas são representadas por paretesis (), mas veja:
# tupla1 = (1, 2, 3, 4, 5, 6)
# print(tupla1)
# print(type(tupla1))
#
# tupla2 = 1, 2, 3, 4, 5, 6
# print(tupla2)
# print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento:
# tupla3 = (2)  # Isso não é uma TUPLA. Sem virgula
# print(tupla3)
# print(type(tupla3))

# tupla4 = (4,)  # Isso é uma TUPLA. Com virgula
# print(tupla4)
# print(type(tupla4))

# tupla5 = 6,  # Isso é uma tupla. Com virgula
# print(tupla5)
# print(type(tupla5))
'''CONCLUSÃO: Tuplas são definidas pelo uso de VIRGULA (',') e não somente pelos PAENTESIS ()'''

# PODEMOS GERAR UMA TUPLA DINAMICAMENTE COM UM RANGE(Inicio, fim, passo)
# tupla7 = tuple(range(11))
# print(tupla7)
# print(type(tupla7))

# DESEMPACOTAMENTO DE TUPLA
# tupla8 = ('Geek University', 'Programação em Python: Essencial')
# escola, curso = tupla8
# print(escola)
# print(curso)

'''METODOS DE ADISSÃO E REMOSÇÃO DE ELEMENTOS NAS TUPLAS NÃO EXISTEM; PORQUE AS TUPLAS SÃO IMUTAVEIS'''
# Soma, Valor Maximo, Valor Minimo e Tamanho: Se os valores foram enteiros e reais
tupla9 = (1, 2, 3, 4, 5, 6)  # Se na tupla existisse letras e numeros(tupla9 = (1, 2, 3, 4, 5, 'b') (sum, max, min) Não
# conseguem processar.
# print(sum(tupla9))
# print(max(tupla9))
# print(min(tupla9))
# print(len(tupla9))

# CONCATENAÇÃO DE TUPLAS
# tupla10 = (1, 2, 3)
# print(tupla10)
#
# tupla11 = (4, 5, 6)
# print(tupla11)

# Modo1: Podemos contanerlas
# print(tupla10 + tupla11)

# print(tupla10)
# print(tupla11)

# Modo2: Se queremos altera uma das tuplas. Craindo uma nova tupla
# tupla12 = tupla10 + tupla11

# print(tupla12)
# print(tupla10)
# print(tupla11)

# Modo3: Podemos sobreescrever os valore da tupla10
# tupla10 = tupla10 + tupla11
# tupla10 += tupla11

# print(tupla10)

# VERIFICAR SE DETERMINANDO ELEMENTO ESTA COTIDO NA TUPLA
# tupla13 = (1, 2, 3)
# print(33 in tupla13)

# ITERANDO SOBRE UMA TUPLA
tupla14 = (1, 2, 3)
# for n in tupla14:
#     print(n)

# for indice, valor in enumerate(tupla14):
#     print(indice, valor)

# CONTANDO ELEMENTOS DENTRO DE UMA TUPLA
# tupla15 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
# print(tupla15.count('c'))

# CONVERTINDO STRING EM TUPLAS
tupla16 = tuple('Alexis Cervantes')
# print(tupla16)

# print(tupla16.count('e'))

# ALGUNAS DICAS NA UTILIZAÇÃO DE TUPLAS
# Como as tuplas são inmutaveis. Devemos usa-las sempre que NÃO PRESISAMOS  modificar os valores em uma coleção
# Exemplo 1:
meses = ('janeiro', 'Febereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
         'Dezembro')
# print(meses)

# ACESSO AOS ELEMENTOS DE UMA TUPLA - Semelhante a uma lista
# print(meses[5])

# ITERAR COM WHILE
# i = 0
# while i < len(meses):
#     print(meses[i])
#     i += 1

# VERIFICAMOS EM QUAL INDICE UM ELEMENTO ESTA NA TUPLA
# print(meses.index('Junho'))

# ISLICING
# tupla[INICIO:FIM:PASSO]
# print(meses[5:9])

'''POR QUE USAR TUPLAS?
1. Tuplas são mais rapidas do que as listas
2. Tuplas deixam seu codigo mais seguro. Porque trabalhar com elementos imutaveis traz segurança para o codigo'''

# COPIANDO UMA TUPLA APRA OUTRA
tupla17 = (1, 2, 3)
# print(tupla17)

# nova_tupla18 = tupla17  # Em tuplas não temos SHALLOW COPY

# print(nova_tupla18)
# print(tupla17)

# outra_tupla19 = (4, 5, 6)

# nova_tupla18 += outra_tupla19

# print(nova_tupla18)
# print(tupla17)

print('Olá, voce está no arquivo TUPLAS...')