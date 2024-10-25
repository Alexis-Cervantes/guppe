"""
Decororadores (decorators)
Decorators?
- São funções;
- Envolvem outras funções e aprimoram seus comportamentos
- São exemplos de HOP - Higher Order Functions;
- Decorators tem uma sintaxe pripria, usando "@" - (Syntact Sugar / Açúcar Sintatico)

-------------------------------------
|       Function Decorator          |
------------------------------------

----------------------------------------|
|    --------------------------------   |
|    |       Function Decorada      |   |
|    --------------------------------   |
|----------------------------------------

"""
# Exemplos: Decorators com funções (Sintaxe não recomendada /  Sem açúcar Sinstático )
def seja_educado(funcao):
    def sendo():
        print('foi um prazer conhecer você')
        funcao()
        print('tenha um otimo dia!')
    return sendo

def saudacao():
    print('seja bem-vindo(a), a esse curso ')

# Testando 1:
teste = seja_educado(saudacao)

