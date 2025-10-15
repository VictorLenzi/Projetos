class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade


class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e sua profissão é {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome} e trabalho como {self.profissao}'
        else:
            return f'Olá, sou {self.nome}'


pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()


print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
