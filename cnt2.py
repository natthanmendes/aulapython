class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = valor

c = Conta("Nathan", 100)
print(c.nome)
print(c.saldo)
c.saldo = -1000