
"""Porque testar nosso codigo?"""

'''Testes automatizados

        Aplicação web
---------------------------------
/           frontend e          /
/           backend            /
---------------------------------
/     testes automatizados      /
---------------------------------
Motivos:
- Reduzir bugs (problemas) no código existente;
- Testes garanten que novos recursos da sua nova app não quebrem (alterem) recursos antigos;
- Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuem corrigidos;
- Testes garantem que a refatoração que costumamos a fazer não tragam novos bugs. 

TDD - Desenvolvimento Guiado por Testes - Test Driving Development - 
    - ESTAGIOS DE DESENVOLVIMENTO: 
      - primeiro vc escreve seu teste primeiro.
      - escreve seu codigo mínimo o suficiente para fazer o testa passar - executar com sucesso
      - refatora o código para fazer a funcionalidade e etsta novamente
      - se o teste passa o recurso é considerado completo.
      - MANTRA de todo desenvolvedor: Red(falhou)  / Green(passou) / Refactor(ajusta se falhou)
     
codigo 
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
# felix = Gato('Felix')
# felix.miar()

# print(felix.nome)

print('Porque testar nossos códigos')
