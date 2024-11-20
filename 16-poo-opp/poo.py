"""
Programação Orientada a Objetos (POO) / Object-Oriented Programming (OOP)

POO -> uriliza mapeamentos de objetos do mundo real para modelos computacionais. Foi pensado para pensar/desenvolver
sistemas

Lenguagem C: Não suporta POO porque ele so suporta programação Estruturada.
Linguagem java : Não suporta paradigma Estruturado porque ele so suporta POO.
Linguagem Python: Multiparadigma (Suporta POO, Programação Estruturada e Programação Funcional)
Principais elementos:
- Clases: Modelo do mundo real representado computacionalmente.
- Atributos: Carateristicas do objeto.
- Méthodo: Comportamento do objeto (funções).
- Construtor: Metodo especial utilizado para criar os objetos.
- Objeto: instancia da clase
______________________________
|     CLASSE (molde)          |
| --------------------------- |
| |     Produto (métohdo)   | |
| |-------------------------| |
| |  (atributos)  +nome     | |
| |               +preço    | |
| |               +desconto | |
| --------------------------- |
_______________________________

---------OBJETOS / INSTANCIAS-----------
-------------------    -----------------
|     Notebook    |    |   Caneta Bic  |
|-----------------|    |----------------
|   R$ 2.500,00   |    |   R$ 2,95     |
|       15%       |    |   5%          |
-------------------    -----------------

CONSTRUTOR = Méthodo Especial para criar objetos a partir se nossa classe.
OBJETOS/INSTANCIAS =
"""
# Sem POO:
# numero = 10
# print(numero)
# print(type(numero))

# nome = 'Alexis'
# print(nome)
# print(type(nome))

# Com POO:
class Produto:
    pass

# Atenção:
# ps4 = Produto()
# print(ps4)
# print(type(ps4))

print('POO')
