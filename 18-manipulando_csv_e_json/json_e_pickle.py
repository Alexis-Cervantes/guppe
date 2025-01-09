"""JSON E PICKLE"""
'''JSON -> JavaScript Object Notation
API -> São meios de comunicação entre os serviços oferecidos por empresas (Ex. Twiter, Facebook, Youtube etc) e 
terceiros(nós desenvolvedores). 
JSON -> em teoria é um diccionario e trabalha com aspas duplas
'''
import json

# Utilzando json de fora basica:
# ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', '2340')}])
# print(type(ret))
# print(ret)

# Utilizando json de forma mais complexa
# class Gato:
#     def __init__(self, nome, raca):
#         self.__nome = nome
#         self.__raca = raca
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def raca(self):
#         return self.__raca
#
# felix = Gato('Felix', 'Viralata')
# print(felix.__dict__)
# ret = json.dumps(felix.__dict__)
# print(ret)

# INTEGRANDO JSON COM PICKLE (pip install jsonpickle)
# import jsonpickle

# class Gato:
#     def __init__(self, nome, raca):
#         self.__nome = nome
#         self.__raca = raca
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def raca(self):
#         return self.__raca
#
# felix = Gato('Felix', 'Viralata')
# ret = jsonpickle.encode(felix)
# print(ret)

# Refatorando a classe - ESCRITA

# import jsonpickle
#
# class Gato:
#     def __init__(self, nome, raca):
#         self.__nome = nome
#         self.__raca = raca
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def raca(self):
#         return self.__raca
#
# felix = Gato('Felix', 'Viralata')
# with open('felix.json', 'w') as arquivo:
#     ret = jsonpickle.encode(felix)
#     arquivo.write(ret)

# Refatorando a classe - LEITURA

# import jsonpickle
#
# class Gato:
#     def __init__(self, nome, raca):
#         self.__nome = nome
#         self.__raca = raca
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def raca(self):
#         return self.__raca
#
# with open('felix.json', 'r') as arquivo:
#     conteudo = arquivo.read()
#     ret = jsonpickle.decode(conteudo)
#     print(ret)
#     print(type(ret))
#     print(ret.nome)
#     print(ret.raca)

print('trabalhando com Json e pikle')




