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
# aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

# aniversario = aniversario.split('/')

# aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

# if aniversario.weekday() == 0:
#     print('Você nasceu em um lunes')
# elif aniversario.weekday() == 1:
#     print('Você nasceu em um martes')
# elif aniversario.weekday() == 2:
#     print('Você nasceu em um miercoles')
# elif aniversario.weekday() == 3:
#     print('Você nasceu em um jueves')
# elif aniversario.weekday() == 4:
#     print('Você nasceu em um viernes')
# elif aniversario.weekday() == 5:
#     print('Você nasceu em um sabado')
# elif aniversario.weekday() == 6:
#     print('Você nasceu em um domingo')

# Formatando datas/horas do padrão americano para o nosso padrão via - strftime() - (string format time)
# dd/mm/yyyy hora:minuto

# hoje = datetime.datetime.today()

# print(hoje)

# hoje_formatado = hoje.strftime('%d/%m/%Y')
# hoje_formatado1 = hoje.strftime('%d/%M/%Y')
# hoje_formatado2 = hoje.strftime('%D/%m/%Y')
# hoje_formatado3 = hoje.strftime('%d/%B/%Y')
# hoje_formatado4 = hoje.strftime('%d/%b/%Y')
# hoje_formatado5 = hoje.strftime('%d de %B de %Y')

# print(hoje_formatado)
# print(hoje_formatado1)
# print(hoje_formatado2)
# print(hoje_formatado3)
# print(hoje_formatado4)
# print(hoje_formatado5)

# Criando função que formata os nomes dos meses do ano em portugues

# def formata_data(data):
#     if data.month == 1:
#         return f'{data.day} de Enero de {data.year}'
#     elif data.month == 2:
#         return f'{data.day} de Febrero de {data.year}'
#     elif data.month == 3:
#         return f'{data.day} de Marzo de {data.year}'
#     elif data.month == 4:
#         return f'{data.day} de Abril de {data.year}'
#     elif data.month == 5:
#         return f'{data.day} de Mayo de {data.year}'
#     elif data.month == 6:
#         return f'{data.day} de Junio de {data.year}'
#     elif data.month == 7:
#         return f'{data.day} de Julio de {data.year}'
#     elif data.month == 8:
#         return f'{data.day} de Agosto de {data.year}'
#     elif data.month == 9:
#         return f'{data.day} de Setiembre de {data.year}'
#     elif data.month == 10:
#         return f'{data.day} de Octubre de {data.year}'
#     elif data.month ==11:
#         return f'{data.day} de Noviembre de {data.year}'
#     elif data.month == 12:
#         return f'{data.day} de Diciembre de {data.year}'

# hoje = datetime.datetime.today()
# print(formata_data(hoje))

# Refatorando nosso codigo anterior (instalando biblioteca 'textblob')
from textblob import TextBlob

# def formatando_data(data): # Não funcioanou por caisa da classe translate que esta descontinuada.
#     return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

# hoje = datetime.datetime.today()
# print(formatando_data(hoje))

# Uma alternativa a classe 'translete' que não esta mais disponivel dentro da biblioteca 'textblod' é a biblioteca
# 'googletrans'. Depois de instalada é so chamar ela:

from googletrans import Translator

frase = "Pythom é ótimo para Machine Learning"

traduzir = Translator()

frase_es = traduzir.translate(frase, dest='es')
tb_es = frase_es.text
tb_es




