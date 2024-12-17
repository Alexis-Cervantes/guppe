"""
Escrevendo em Arquivos CSV
reader() -> Leitor;
writer() -> Escritor;
writerow() -> Escreve uma linha
"""
# writer(): gera um objeto para que possamos escrever em um arquivo csv.
# writerow(): utiizado as linhas do arquivo .csv criado anteriormente. Ele receve uma lista

# Trabalhando com WRITER
from csv import writer

# Se queremos acrecentar mas elementos usamos 'a' em vez de 'w'
# with open('filmes.csv', 'w', encoding='utf8') as arquivo:
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['TÍtulo', 'Gênero', 'Duração'])
#     while filme != 'sair':
#         filme = input('Informe o nome do filme: ')
#         if filme != 'sair':
#             genero = input('Informe o Gênero: ')
#             duracao = input('Informe a Duração (em minutos): ')
#             escritor_csv.writerow([filme, genero, duracao])

# Trabalhando com DictWriter
from csv import DictWriter
from pickletools import stringnl_noescape_pair

# with open('filmes2.csv', 'w', encoding='utf8') as arquivo:
#     cabecalho = ['Título', 'Gênero', 'Duração']
#     escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
#     escritor_csv.writeheader()
#     filme = None
#     while filme != 'sair':
#         filme = input('Informe o nome do Filme: ')
#         if filme != 'sair':
#             genero = input('Informe o Gênero: ')
#             duracao = input('Informe a Duração (em minutos): ')
#             escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})






