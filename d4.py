class Ingresso:
    def __init__(self, evento, preco):
        self.evento = evento
        self.preco = preco

    def calcular_preco(self):
        return self.preco

    def __str__(self):
        return f"Ingresso para {self.evento} - R${self.calcular_preco():.2f}"

    def __repr__(self):
        return f"Ingresso(evento='{self.evento}', preco={self.preco})"


