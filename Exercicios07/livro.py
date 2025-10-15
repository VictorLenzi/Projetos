class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'O título do livro é {self.titulo}, o autor(a) é o(a) {self.autor} e o ano de publicação foi em {self.ano_publicacao} e ele está disponivel? {self.disponivel}'

    def emprestar(self):
        self._disponivel = False

    @property
    def disponivel(self):
        return '✅' if self._disponivel else '❌'

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [
            livro for livro in Livro.livros if livro.ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis


primeiro_livro = Livro('Ao Farol', 'Virginia Woolf', 1927)
segundo_livro = Livro('A casa dos espíritos', 'Isabel Allende', 1982)

segundo_livro.emprestar()

print(primeiro_livro)
print(segundo_livro)

livros_disponiveis_ano = Livro.verificar_disponibilidade(1927)
for livro in livros_disponiveis_ano:
    print(f'Livro Disponivel no ano selecionado: {livro.titulo}')
