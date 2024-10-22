"""
Escrevendo um Iterador Customizado
"""
from blib2to3.pgen2.driver import ReleaseRange


# Vammos fazer um iterador parecido a do que faz um for/range
# for n in range(0, 11):
#     print(n)

class Contador:  # a seguinte função são chamados de COSTRUTORES
    def __init__(self, menor, maior):  # Funções dentro de Clases se chamam METODOS
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration

# Vamos inteagir com essa classe:
# con = Contador(1, 6)
# print(con) # saida: <__main__.Contador object at 0x000002474D64DC40>

# print(con.menor) # saida -> 1
# print(con.maior) # saida -> 50

# Vamos tranforar essa variavel em um ITERABLE
# it = iter(con) # para corregir esse erro temos que modificar nossa clase. Acrecentar mais coisas
# print(next(it)) # saida -> TypeError: 'Contador' object is not iterable
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# Fazendo o mesmo porem com FOR in:
for n in Contador(1, 6):
    print(n) # saida-> 1, 2, 3, 4, 5

# range faz o mesmo:
for n in range(1, 6):
    print(n) # saida-> 1, 2, 3, 4, 5



