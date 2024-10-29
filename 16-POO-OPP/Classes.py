"""
POO - Classes: São objetos do mundo real representadoscomputacionalmente.

Exemplo: Digamos você quera criar um sostemas para sistematizar o controle das suas lampadas
Classes: podem conter:
- Atributos: representam as carateristicas do objeto. Ou seja pelos atributos conseguimos representar elas
computacionalmenteos estados de um objeto. No caso da Lampada, possivelmente iriamos querer saber s eela é de 110 ou
220 vlts, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela.

- Métodos: (funções) Representam o comportamento do objeto. Ou seja as ações que esse objeto pde realizar no seu
sistema. No caso da lampada um comportamento que nos iriamos querer saber é o ligar / desligar.

- Em python para definir uma clase utilizamos a palavra reservada 'class'
- pass é usado para prencher o conteudo da classe que não faz nada
"""
from symtable import Class

# SEM POO:
# idade = 50
# preco = 2340.45
# nome = 'alexis'

# print(type(idade))
# print(type(preco))
# print(type(nome))

# POO
class Lampada:
    pass

lamp = Lampada()
print(type(lamp))
