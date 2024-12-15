"""Lendo arquivos CSV

CSV -> Comma Separeted Values (Valores separados por virgula)'''

Seaparador por virgula:
Exe
1, 2, 3, 4, 5
Maria, Alexis, Cacia, Eduarda

Separador por ponto e virgula:
Exe:
1; 2; 3; 4; 5
Maria; Alexis; Cacia; Eduarda

Separador por Espaço:
1 2 3 4 5
Maria Alexis Cacia Eduarda

http://dados.gov.br/dataset
"""
# # Muito trabalhosso: leitura de arquivos CSV
# with open('lutadores.csv', encoding='utf8') as arquivo:
#     dados = arquivo.read()
#     # print(type(dados))
#     # Limpeza de Dados: (.split: para separar as informações com virgula /  Slice: para comezar da segunda linha
#     dados = dados.split(',')[2:]
#     print(dados)

# Forma Certa para ler arqivos CSV: Existem dois modos:
"""
- Reader: Permite itereção sobre as linhas do arquivo csv como listas;
- DicReader: Permite ieteração sobre as linhas do arquivo csv como OrderedDicst;
"""
# Reader: Importando biblioteca:
from csv import reader

# with open('lutadores.csv', encoding='utf8') as arquivo:
#     leitor_csv = reader(arquivo)
#     next(leitor_csv) # Pular o cabeçalho
#     for linha in leitor_csv:
#         # OBS: cada linha é uma lista:
#         print(f'{linha[0]}, nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')


# DictReader: Importando biblioteca:
from csv import DictReader
# OBS: DictReader tem como padrão trabalhar com a (,) como delimitador

# with open('lutadores.csv', encoding='utf8') as arquivo:
#     leitor_csv = DictReader(arquivo)
#     for linha in leitor_csv:
#         # OBS: cada linha é uma Ordered Dict:
#         print(f"{linha['Nome']}, nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")


# DictReader: Com outro delimitador(exe. ';', '/', '\' etc)

# with open('lutadores.csv', encoding='utf8') as arquivo:
#     leitor_csv = DictReader(arquivo, delimiter=',')
#     for linha in leitor_csv:
#         # OBS: cada linha é uma Ordered Dict:
#         print(f"{linha['Nome']}, nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

print('lendo arquivo csv')