class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)


class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0, ativo=False):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = ativo
        self._capacidade = capacidade
        self._nota_avaliacao = nota_avaliacao
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'O nome do restaurante é {self._nome} e a categoria é {self._categoria}, {self.ativo}'

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        self._ativo = not self._ativo

    @classmethod
    def listar_restaurantes(cls):
        print(
            f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(
                f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')


restaurante_formatado = Restaurante(
    nome='comida Delicia', categoria='Almoço', ativo=False)
restaurante_formatado.alternar_estado()
print(restaurante_formatado)

novo_restaurante = Restaurante(
    nome='Comida Boa', categoria='Gourmet', capacidade=50, nota_avaliacao=4.5, ativo=True)

# novo restaurante utilizando o construtor
novo_restaurante_construtor = Restaurante(
    nome='Santa Marmita', categoria='Fast Food')


class Cliente:

    def __init__(self, nome, idade, estado, area=''):
        self.nome = nome
        self.idade = idade
        self.estado = estado
        self.area = area

    def __str__(self):
        return f'Cliente {self.nome} tem {self.idade} anos e é de {self.estado}'


cliente1 = Cliente(nome='Junior', idade='60', estado='SC')
print(cliente1)
