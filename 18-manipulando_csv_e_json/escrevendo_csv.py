"""
Escrevendo em Arquivos CSV
reader() -> Leitor;
writer() -> Escritor;
writerow() -> Escreve uma linha
"""
# writer(): gera um objeto para que possamos escrever em um arquivo csv.
# writerow(): utiizado as linhas do arquivo .csv criado anteriormente. Ele receve uma lista

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duaração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])


