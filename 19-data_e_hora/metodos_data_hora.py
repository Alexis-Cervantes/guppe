"""Métodps Data e Hora"""

import datetime

# agora = datetime.datetime.now()
# Com 'now' podemos especificar um time zone (fuso horario)
# print(agora)
# print(type(agora))
# print(repr(agora))

# hoje = datetime.datetime.today()

# print(hoje)
# print(type(hoje))
# print(repr(hoje))

# Mudanças ocorridas a meia noite:
# manutecao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
# print(manutecao)
# print(type(manutecao))
# print(repr(manutecao))

# Encontrando o dia da semana: weekday()

# Os dias das semana do méthodo 'weekday'
# 0 - lunes (Monday)
# 1 - martes (tuesday)
# 2 - miercoles (wednesday)
# 3 - jueves (thursday)
# 4 - viernes (friday)
# 5 - sabado (saturday)
# 6 - domingo (sunday)

# manutecao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

# print(manutecao.weekday())

# Encontrar o data de nascimento
aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em um lunes')
elif aniversario.weekday() == 1:
    print('Você nasceu em um martes')
elif aniversario.weekday() == 2:
    print('Você nasceu em um miercoles')
elif aniversario.weekday() == 3:
    print('Você nasceu em um jueves')
elif aniversario.weekday() == 4:
    print('Você nasceu em um viernes')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sabado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um domingo')

