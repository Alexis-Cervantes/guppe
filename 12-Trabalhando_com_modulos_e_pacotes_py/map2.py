import math
"""Map - Duplicada para trabalhar com importação de modulos"""

# Exemplo 1: criando uma função


def area(r):
    """Calcula a área do circulo com um raio 'r' """
    return math.pi * (r ** 2)

# print(area(2))
# print(area(5.3))


# Exemplo 2: Digamos que temos uma lista contendo varios valores de raios e querenmos calcular todas elas.
raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma 1: Comum
areas_1 = []
for r in raios:
    areas_1.append((area(r)))

# print(areas_1)

# Forma 2: map
areas_2 = map(area, raios)

# print(areas_2)  # Retorna um map object
# print(type(areas_2))  # retorna class map

# print(list(areas_2))  # print(tupla(areas_2))

# Umas forma mais rapide e eficiente: Menos codigo
# print(list(map(area, raios)))

'''UTILIZANDO UMA FUNÇÃO LAMBDA'''
# Forma 3: map + lambda -  MAGIA PURA
# print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Outro exemplo: Digamos que queremos converter os grados 'Cº' em 'Fº'

cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('New York', 28),
           ('Londres', 22)]
# print(cidades)

# formula para converter Cº em fº: f = 9/5 * c + 32

# lambda:
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

# print(list(map(c_para_f, cidades)))

# poderia ser assim tambem: Menos codigo
# print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))

# print('Olá você esta no arquivo Map2 - Duplicada para ser trabalhada no arquivo modulos customizados')