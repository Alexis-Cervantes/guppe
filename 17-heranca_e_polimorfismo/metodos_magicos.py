"""
POO - MÉTODOS MÁGICOS
São todos os métodos que utilizam 'dunder'
Dunder -> Double Underscore -
EXE.
1) dunder: def __init__(self)

2) dunder: def __repr__(self) -> Representação do objeto

3) dunder: def __str__(self) -> Representação de string - prevalencia entre ele e dunder repr

"""
class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('um objeto de tipo Livro foi deletado da Memória')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ' '
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'

# livro1 = Livro('Python Rocks!', 'Alexis Cervantes', 400)
# livro2 = Livro('Inteligência Articial com Pythom', 'Eduarda Cervantes', 350)

# print(livro1)
# print(livro2)

# print(len(livro1))
# print(len(livro2))

# print(livro1 + livro2)

# print(livro1 * 5)

print('métodos mágicos')