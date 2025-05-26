class Conta:

    JUROS = 10
    def __init__(self, nome, saldo=0):
        self.__nome = nome
        self.__saldo = int(saldo)

    # getters and setters
    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_saldo(self):
        return self.__saldo


    def deposito(self, valor_deposito):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
        else:
            print("O valor a depositar deve ser maior que 0!")

    def saque(self, valor_saque):
        if valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
        else:
            self.__saldo -= valor_saque - Conta.JUROS