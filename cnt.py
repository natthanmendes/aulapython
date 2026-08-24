class Conta:
   def __init__(self, descricao, valor, vencimento, status):
       self.descricao = descricao
       self.valor = valor
       self.vencimento = vencimento
       self.status = status


   def pagar(self):
       self.status = "Pago"

contas = []

while True:

   print("\n===== MENU =====")
   print("1 - Cadastrar conta")
   print("2 - Pagar conta")
   print("3 - Exibir contas")
   print("4 - Exibir contas pendentes")
   print("5 - Sair")

   opcao = input("Escolha uma opção: ")

   if opcao == "1":

       descricao = input("Digite a descrição da conta: ")
       valor = float(input("Digite o valor da conta: "))
       vencimento = input("Digite o vencimento: ")

       conta = Conta(descricao, valor, vencimento, "Não pago")
       contas.append(conta)

       print("Conta cadastrada com sucesso!")
       print("ID da conta:", len(contas) - 1)

   elif opcao == "2":

       if len(contas) == 0:
           print("Não existem contas cadastradas.")

       else:
           print("\n===== CONTAS =====")

           for i in range(len(contas)):
               print(
                   i,
                   "-",
                   contas[i].descricao,
                   "- R$",
                   contas[i].valor,
                   "-",
                   contas[i].status
               )

           id_conta = int(input("Digite o ID da conta que deseja pagar: "))

           if id_conta >= 0 and id_conta < len(contas):
               contas[id_conta].pagar()
               print("Conta paga com sucesso!")
           else:
               print("ID inválido.")

   elif opcao == "3":

       print("\n===== TODAS AS CONTAS =====")

       if len(contas) == 0:
           print("Não existem contas cadastradas.")

       else:
           for i in range(len(contas)):
               print(
                   "ID:", i,
                   "| Descrição:", contas[i].descricao,
                   "| Valor: R$", contas[i].valor,
                   "| Vencimento:", contas[i].vencimento,
                   "| Status:", contas[i].status
               )

   elif opcao == "4":

       print("\n===== CONTAS PENDENTES =====")

       encontrou = False

       for i in range(len(contas)):

           if contas[i].status == "Não pago":
               print(
                   "ID:", i,
                   "| Descrição:", contas[i].descricao,
                   "| Valor: R$", contas[i].valor,
                   "| Vencimento:", contas[i].vencimento
               )

               encontrou = True

       if encontrou == False:
           print("Não existem contas pendentes.")

   elif opcao == "5":

       print("Programa encerrado.")
       break

   else:
       print("Opção inválida!")



