"""Manipulando Data e Hora"""
from pydoc import replace

'''
Python tem um modulo Built-in (integrado) para se trabalhar com data e hora - datetime
'''
import datetime

# print(dir(datetime))
# SAIDA:
'''['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 
'tzinfo']'''

# Interafindo com alguns elementos:

# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)
# Mostrar a data e hora corrente
# print(datetime.datetime.now()) # -> 2025-01-09 08:58:01.059392 / formato diferente que o brasileiro - BR 09/01/2025

# datetime.datetime(year, month, day, hour, minute, second, microsecund)
# print(repr(datetime.datetime.now())) # -> datetime.datetime(2025, 1, 9, 9, 0, 48, 864103)

# replace() -> para fazer ajustes na data/hora
# inicio = datetime.datetime.now()
# print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
# inicio = inicio.replace(year=2030, hour=16, minute=0, second=0, microsecond=0)
# print(inicio)

# É possivel criar uma data hora
evento = datetime.datetime(1974, 6, 26,0)
print(evento)
