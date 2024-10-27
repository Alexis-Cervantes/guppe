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
from xml.sax.handler import property_interning_dict

# Decorators com funções (Sintaxe não recomendada /  Sem açúcar Sinstático )
# def seja_educado(funcao):     # Decrators Function/Função decoradora:
#     def sendo():
#         print('foi um prazer conhecer você')
#         funcao()
#         print('tenha um otimo dia!')
#     return sendo

# def saudacao():
#     print('seja bem-vindo(a), a esse curso ')

# Testando a função saudacao:
# saudacao()

# Testando 1 - agora vamos decorarla:

# teste = seja_educado(saudacao)        # Decorator aplicada
# teste() # Aprimoramos a função

# Testando 2:
# def raiva():
#     print('EU TE ODEIO')

# raiva_educada = seja_educado(raiva)

# raiva_educada()

# decorators com Syntax Sugar (Açúcar Sintático)
# def seja_educado_mesmo(funcao):
#     def sendo_mesmo():
#         print('Foi um prazer conhecer você!')
#         funcao()
#         print('Tenha um excelente día!')
#     return sendo_mesmo

# @seja_educado_mesmo
# def dormir():
#     print('Quero dormir...')

# def apresentando():
#     print('Meu nome é Pedro')

# Testando apresentando:
# apresentando()

# Testando dormir:
# dormir()

# Exemplo de website:
'''
-------------------------------------------------------
|    Home    Serviçõs    Produtos    Administrativo   |
-------------------------------------------------------
http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/Serviçõs
http://www.suaempresa.com.br/Produtos
http://www.suaempresa.com.br/Administrativo

OBS: Não é codigo funcional (que funciones) é apenas exemplo:

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')

def home(request):
    return 'pode acessar home'
    
def servicos(request):
    return 'pode acessar serviços'

def produtos(request):
    return 'pode acessar produtos'

@checa_login
def admin(request):
    return 'pode acessar admin'
'''

print('decoradores')
