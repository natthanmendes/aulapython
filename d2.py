class Entrega:
    def __init__(self, distancia, peso):
        self.distancia = distancia
        self.peso = peso

    def calcular_frete(self):
        return 0

class EntregaComum(Entrega):
    def calcular_frete(self):
        return (self.distancia * 2) + (self.peso * 1)

class EntregaExpressa(Entrega):
    def calcular_frete(self):
        return (self.distancia * 3.50) + (self.peso * 2) + 10

while True:

    print("\n------ SISTEMA DE ENTREGAS ------")

    tipo = input("Qual tipo de entrega você quer? (Comum/Expressa): ")

    distancia = float(input("Digite a distância em km: "))
    peso = float(input("Digite o peso em kg: "))

    if tipo == "Comum":
        entrega = EntregaComum(distancia, peso)

    elif tipo == "Expressa":
        entrega = EntregaExpressa(distancia, peso)

    else:
        print("Tipo de entrega inválido")
        continue

    print("\n------ DADOS DA ENTREGA ------")

    print("Tipo:", tipo)
    print("Distância:", distancia, "km")
    print("Peso:", peso, "kg")
    print(f"Frete: R$ {entrega.calcular_frete():.2f}")

    cadastrar = input("\nDeseja cadastrar outra entrega? (S/N): ")

    if cadastrar == "N":
        print("Programa encerrado")
        break