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


class IngressoInteiro(Ingresso):
    def calcular_preco(self):
        return self.preco

    def __str__(self):
        return f"Ingresso Inteiro para {self.evento} - R${self.calcular_preco():.2f}"

    def __repr__(self):
        return f"IngressoInteiro(evento='{self.evento}', preco={self.preco})"


class MeiaEntrada(Ingresso):
    def calcular_preco(self):
        return self.preco * 0.5

    def __str__(self):
        return f"Meia-entrada para {self.evento} - R${self.calcular_preco():.2f}"

    def __repr__(self):
        return f"MeiaEntrada(evento='{self.evento}', preco={self.preco})"


def menu():
    print("\n--- Compra de Ingressos ---")
    evento = input("Digite o nome do evento: ")
    preco = float(input("Digite o preço do ingresso: "))

    print("\nEscolha o tipo de ingresso:")
    print("1 - Inteira")
    print("2 - Meia-entrada")
    opcao = input("Opção: ")

    if opcao == "1":
        ingresso = IngressoInteiro(evento, preco)
    elif opcao == "2":
        ingresso = MeiaEntrada(evento, preco)
    else:
        print("Opção inválida!")
        return

    print("\nCompra realizada com sucesso!")
    print(str(ingresso))
    print(repr(ingresso))


menu()

