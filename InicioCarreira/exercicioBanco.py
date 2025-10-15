class ContaBancaria:
    def __init__(self, titular='', saldo=0, ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return f'O titular da conta é {self._titular}, e tem saldo de {self._saldo} e a conta está {self.ativo}'

    def ativar_conta(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'


primeiro_titular = ContaBancaria(titular='Victor', saldo=1000)
segundo_titular = ContaBancaria(titular='Fernando', saldo=800)

primeiro_titular.ativar_conta()

print(primeiro_titular)
print(segundo_titular)


terceiro_titular = ContaBancaria("Fernanda", 1500)
print(terceiro_titular)


class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta


cliente1 = ClienteBanco("Victor", 24, "Rua Exemplo 1",
                        "123.456.789-00", "Desenvolvedor")
cliente2 = ClienteBanco("Ana", 25, "Rua Exemplo 2", "987.654.321-00", "CEO")
cliente3 = ClienteBanco("Vinicius", 30, "Rua Exemplo 3",
                        "147.258.369-00", "Gerente de Operações")

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(
    f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
