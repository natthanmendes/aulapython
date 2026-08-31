import logging

logging.basicConfig(
    filename="arquivo_log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def processar_pedido():
    logging.info("A função foi chamada pelo usuário com os valores")

    nome_cliente = input("Nome do cliente: ")
    nome_produto = input("Nome do produto: ")

    try:
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: R$ "))

        logging.debug(
            f"Dados recebidos: cliente={nome_cliente}, "
            f"produto={nome_produto}, quantidade={quantidade}, "
            f"valor={valor_unitario}"
        )

        if quantidade <= 0:
            logging.warning("Quantidade igual a zero ou valor negativo.")
            print("Erro: a quantidade deve ser maior que zero.")
            return

        valor_total = quantidade * valor_unitario

        logging.info("Pedido processado com sucesso.")

        print("\n--- PEDIDO ---")
        print(f"Cliente: {nome_cliente}")
        print(f"Produto: {nome_produto}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor unitário: R$ {valor_unitario:.2f}")
        print(f"Valor total: R$ {valor_total:.2f}")

    except ValueError:
        logging.error("Erro durante a entrada ou processamento dos dados.")
        print("Erro: digite valores válidos.")


while True:

    print("\n===== SISTEMA DE PEDIDOS =====")
    print("1 - Processar pedido")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        processar_pedido()

    elif opcao == "2":
        logging.info("Programa encerrado pelo usuário.")
        print("Programa encerrado.")
        break

    else:
        logging.warning("Opção inválida selecionada pelo usuário.")
        print("Opção inválida!")

