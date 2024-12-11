"""Lendo arquivos CSV

CSV -> Comma Separeted Values (Valores separados por virgula)'''

Seaparador por virgula:
EXE
1, 2, 3, 4, 5
Maria, Alexis, Cacia, Eduarda

Separador por ponto e virgula:
EXE:
1; 2; 3; 4; 5
Maria; Alexis; Cacia; Eduarda

Separador por Espaço:
1 2 3 4 5
Maria Alexis Cacia Eduarda

http://dados.gov.br/dataset
"""
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    print(dados)
