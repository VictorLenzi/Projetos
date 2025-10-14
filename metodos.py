class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)


class Restaurante:

    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

    def __str__(self):
        return f'O nome do restaurante é {self.nome} e a categoria é {self.categoria}'


restaurante_formatado = Restaurante(nome='Comida Delicia', categoria='Almoço')
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
