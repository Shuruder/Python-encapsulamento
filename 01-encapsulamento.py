# Encapsulamento em Python é uma convenção, ou seja, temos padrões que definem o funcionamento pois eles não importam para o compilador
# No caso o encapsulamento de variaveis se dá pelo Underline _
# No exemplo abaixo temos o saldo como variavél privada, que só deve ser trabalhada dentro de sua classe

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())