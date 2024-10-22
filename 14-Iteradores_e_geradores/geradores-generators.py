"""
Geradores = (GENERATORS) e são iteradores (ITERATORS);
OBS: O contrario não é verdadero. Ouse ja, nem thodo ITERATOR é um Gerador (GENERATOR)

OUTRAS INFORMAÇÕES:
- GENERATOS podem ser criados com funções GERADORAS;
- Funções GERADORAS usam a palavra reservada 'yield';
- GENERATORS podem ser criados com Expressões Geradoras;

DIFERENÇA ENTRE FUNÇOES E GENERATOR FUNCTIONS (Funções geradoras)
-----------------------------------------------------------------------------------
|   Funções                             |   Generator Functions                    |
------------------------------------------------------------------------------------
|   Utilizam return                     |   Utilizam yield                          |
------------------------------------------------------------------------------------
|   Retorna uma vez                     |   Podem utilizar yield multiplas vezes    |
-------------------------------------------------------------------------------------
|   Quando executada - retorna um valor |   Quando executada, retorna um generator  |
-------------------------------------------------------------------------------------
"""

# Exemplo de Generator Function (Função Gereadora):
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador +=1

# OBS: Um Generator Function não é um Generator. Ela gera um Generator

# gen = conta_ate(5)
# print(type(gen)) # <class 'generator'>

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen)) # Se colocamos 1 print más va a ocurrir um erro -StopIteration

# vamos itera com for:
# gen = conta_ate(10)
# for num in gen:
#     print(num)

# gen = conta_ate(10)
# print(next(gen))
# print('alexis')
#
# for num in gen: # va começar a partir de 2
#     print(num)

# Se queremos fazer thodo de vez
# gen = list(conta_ate(10))
# print(gen)

print('Generator')