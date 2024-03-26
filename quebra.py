def interface_usuario(produtos):
    input("Bem-vindo à nossa Distribuidora de Bebidas! Pressione Enter para ver os produtos.")
    exibir_produtos(produtos)

    while True:
        try:
            escolha_codigo = int(
                input("\nDigite o código do produto desejado: "))
            escolha_quantidade = int(input("Digite a quantidade desejada: "))
            break
        except ValueError:
            print("Por favor, digite valores numéricos para o código e a quantidade.")

    return escolha_codigo, escolha_quantidade
