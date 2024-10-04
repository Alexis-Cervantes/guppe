"""Modulo Random"""

'''
- Em Python, modulos nada mais são do que outros arquivos python
- Modulo Random: possue varias funções para geração de número real pseudo-aleatório
'''
# OBS: Existem duas formas de se utilizar um módulo ou função deste:

# Forma 1: Importando thodo o modulo (Não recomendado)
# import random
# OBS: Ao realizar o import de thodo o módulo, thodas as funções, atributos, classes e propriedades que estiverem dentro
# do módulo ficarão disponiveis (Ficarão em memoria). Caso você saiba quais funções você precisa utilizar deste
# módulo, então esta não seria a forma ideal de utilização.

# print(dir(random))  # Com dir podemos saber todas as funções do módulo random
'''['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', 
'_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
 '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', 
 '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', 
 '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 
 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 
 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate',
  'weibullvariate']
'''
# print(help(random.random))  # Com help podemos saber o que faz a função random do módulo random
'''
random() method of random.Random instance
    random() -> x in the interval [0, 1).

None'''

# print(random.random())  # 0.6387051018533141 / Módulo random.função random

# Forma 2: Importando um função especifica do módulo - Forma recomendada
# Importando:
from random import random

# for i in range(10):
#     print(random())

# Uniform() -> Gera um numero real pseudo-aleatorio entre os valores estabelecidos
# Importando:
from random import uniform
# for i in range(10):
#     print(uniform(3,7))  # 7 não é incluido

# randint()  -> gera valores inteiros pseudo-aleatorios entre valores estabelcidos
from random import randint
# for i in range(6):
#     print(randint(1, 61), end=', ')  # Começa em 1 e vai at´r 60

# choice()  ->  Mostra um avalor aleató rio emtre um iteravel
from random import choice

# jogadas = ['pedra', 'papel', 'tisoura']
# print(choice(jogadas))

# print(choice('Alexis Cervantes'))

# shuffle()  -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['Q', 'k', 'j', 'A', '2', '3', '4', '5', '6', '7']

# print(cartas)
# shuffle(cartas)
# print(cartas)  #  Embaralhado de todas as cartas
# print(cartas[0])  # Mostra uma carta
# print(cartas.pop)  # Com pop tiramos a ultima carta

print("OLá vc esta no arquivo modulo random")

