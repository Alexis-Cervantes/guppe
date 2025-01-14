"""Porque testar nosso codigo"""
'''Testes automatizados

---------------------------------
/           front end           /
/           back end            /
---------------------------------
/     testes automatizados      /
---------------------------------
Motivos:
- Reduzir bugs (problemas) no código existente;
- Testes garanten que novos recursos da sua nova app não quebrem (alterem) recursos antigos;
- Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuem corrigidos;
- Testes garantem que a refatoração que costumamos a fazer não tragam novos bugs. 

TDD - Desenvovlvimento Guiado por Testes - Test Driving Development 
'''
class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')

# Testando nossa classe de forma MANUAL - BÁSICOS
felix = Gato('Felix')
felix.miar()

print(felix.nome)

