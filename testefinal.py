from abc import ABC, abstractmethod

# Classe abstrata representando um item de venda (Interfaces e/ou Classes Abstratas)


class ItemVenda(ABC):
    def __init__(self, codigo, nome, preco_unitario, estoque):
        # Encapsulamento: Atributos protegidos (não diretamente acessíveis de fora da classe)
        self._codigo = codigo
        self._nome = nome
        self._preco_unitario = preco_unitario
        self._estoque = estoque

    # Métodos abstratos que devem ser implementados pelas subclasses (Contrato)
    @abstractmethod
    def exibir_informacoes(self):
        pass

    @abstractmethod
    def atualizar_estoque(self, quantidade):
        pass

    @abstractmethod
    def calcular_valor_total(self, quantidade):
        pass


# Classe concreta representando um produto (Herança e Polimorfismo)
class Produto(ItemVenda):
    def exibir_informacoes(self):
        print(f"Código: {self._codigo}")
        print(f"Produto: {self._nome}")
        print(f"Preço Unitário: R${self._preco_unitario:.2f}")
        print(f"Estoque Disponível: {self._estoque} unidades")

    def atualizar_estoque(self, quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        else:
            print("Estoque insuficiente.")
            return False

    def calcular_valor_total(self, quantidade):
        return self._preco_unitario * quantidade


# Classe concreta representando um serviço (Herança e Polimorfismo)
class Servico(ItemVenda):
    def exibir_informacoes(self):
        print(f"Código: {self._codigo}")
        print(f"Serviço: {self._nome}")
        print(f"Preço Unitário: R${self._preco_unitario:.2f}")

    def atualizar_estoque(self, quantidade):
        print("Operação não suportada para serviços.")

    def calcular_valor_total(self, quantidade):
        return self._preco_unitario * quantidade


# Factory Method para criar itens de venda (Padrão de Projeto Factory Method)
class ItemVendaFactory(ABC):
    @abstractmethod
    def criar_item_venda(self, codigo, nome, preco_unitario, estoque):
        pass


class ProdutoFactory(ItemVendaFactory):
    def criar_item_venda(self, codigo, nome, preco_unitario, estoque):
        return Produto(codigo, nome, preco_unitario, estoque)


class ServicoFactory(ItemVendaFactory):
    def criar_item_venda(self, codigo, nome, preco_unitario, estoque):
        return Servico(codigo, nome, preco_unitario, estoque)


# Função para exibir os produtos disponíveis
def exibir_produtos(produtos):
    print("Produtos Disponíveis:")
    for produto in produtos:
        produto.exibir_informacoes()
        print("----------------")


# Função para dar as boas-vindas e solicitar o pedido do cliente
def interface_usuario(produtos):
    input("Bem-vindo à nossa Distribuidora de Bebidas! Pressione Enter para ver os produtos.")
    exibir_produtos(produtos)
    print("\nQual é o seu pedido?")
    escolha_codigo = int(input("Digite o código do produto desejado: "))
    escolha_quantidade = int(input("Digite a quantidade desejada: "))
    return escolha_codigo, escolha_quantidade


if __name__ == "__main__":
    # Criando Factory Methods
    produto_factory = ProdutoFactory()
    servico_factory = ServicoFactory()

    # Criando alguns produtos e serviços
    produtos_em_estoque = [
        produto_factory.criar_item_venda(1, "Cerveja", 3.50, 50),
        produto_factory.criar_item_venda(2, "Refrigerante", 2.00, 30),
        produto_factory.criar_item_venda(3, "Suco", 4.00, 20),
    ]

    # Interface do usuário
    escolha_codigo, escolha_quantidade = interface_usuario(produtos_em_estoque)

    # Encontrando o produto escolhido na lista
    produto_escolhido = None
    for produto in produtos_em_estoque:
        if produto._codigo == escolha_codigo:  # Encapsulamento: Atributo acessado indiretamente
            produto_escolhido = produto
            break

    if produto_escolhido is not None:
        # Verificando e processando a venda (Polimorfismo)
        if isinstance(produto_escolhido, Produto):
            if produto_escolhido.atualizar_estoque(escolha_quantidade):
                print("\nResumo da Venda:")
                produto_escolhido.exibir_informacoes()
                print(f"Quantidade: {escolha_quantidade}")
                print(f"Total: R${produto_escolhido.calcular_valor_total(
                    escolha_quantidade):.2f}")
            else:
                print("Venda não realizada devido a estoque insuficiente.")
        else:
            print("Operação não suportada para serviços.")
