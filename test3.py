class Produto:
    def __init__(self, codigo, nome, preco_unitario, estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.estoque = estoque

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}")
        print(f"Produto: {self.nome}")
        print(f"Preço Unitário: R${self.preco_unitario:.2f}")
        print(f"Estoque Disponível: {self.estoque} unidades")

    def atualizar_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print("Estoque insuficiente.")
            return False


class Venda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.produto.preco_unitario * self.quantidade

    def exibir_recibo(self):
        print("Recibo da Venda")
        print("================")
        self.produto.exibir_informacoes()
        print(f"Quantidade: {self.quantidade}")
        print(f"Total: R${self.calcular_valor_total():.2f}")


# Função para exibir os produtos disponíveis
def exibir_produtos(produtos):
    print("Produtos Disponíveis:")
    for produto in produtos:
        produto.exibir_informacoes()
        print("----------------")


# Função para dar as boas-vindas e solicitar o pedido do cliente
def interface_usuario(produtos):
    print("Bem-vindo à nossa Distribuidora de Bebidas!")
    exibir_produtos(produtos)
    print("\nQual é o seu pedido?")
    escolha_codigo = int(input("Digite o código do produto desejado: "))
    escolha_quantidade = int(input("Digite a quantidade desejada: "))
    return escolha_codigo, escolha_quantidade


# Exemplo de uso
if __name__ == "__main__":
    # Criando alguns produtos
    cerveja = Produto(1, "Cerveja", 3.50, 50)
    refrigerante = Produto(2, "Refrigerante", 2.00, 30)
    suco = Produto(3, "Suco", 4.00, 20)

    # Lista de produtos em estoque
    produtos_em_estoque = [cerveja, refrigerante, suco]

    # Interface do usuário
    escolha_codigo, escolha_quantidade = interface_usuario(produtos_em_estoque)

    # Encontrando o produto escolhido na lista
    produto_escolhido = None
    for produto in produtos_em_estoque:
        if produto.codigo == escolha_codigo:
            produto_escolhido = produto
            break

    if produto_escolhido is not None:
        # Verificando e processando a venda
        if produto_escolhido.atualizar_estoque(escolha_quantidade):
            venda_cliente = Venda(produto_escolhido, escolha_quantidade)
            print("\nResumo da Venda:")
            venda_cliente.exibir_recibo()
        else:
            print("Venda não realizada devido a estoque insuficiente.")
