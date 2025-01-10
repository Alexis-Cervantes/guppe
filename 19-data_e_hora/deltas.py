"""Trabalhando de Deltas de data e hora"""

'''
data_inicial = dd/mm/yyyy 12:55:34.984562
data_final = dd/mm/yyyy 13:58:44.084962

delta = data_final - data_inicial
'''
import datetime

# data de hoje
# data_hoje = datetime.datetime.now()

# data para ocorrer um determinado evento futuro
# aniversario = datetime.datetime(2025, 6, 26, 0)

# calculando o delta
# tempo_para_evento = aniversario - data_hoje

# print(type(tempo_para_evento))
# print(repr(tempo_para_evento))
# print(tempo_para_evento)

# para especificar dias
# print(tempo_para_evento.days)

# Para ser mais preciso (detalhes)
# print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60 } horas')

# Ecommercer
data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)
