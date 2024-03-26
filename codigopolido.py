class Bebida:
    def __init__(self, nome, tipo, volume_ml, teor_alcoolico):
        self.nome = nome
        self.tipo = tipo
        self.volume_ml = volume_ml
        self.teor_alcoolico = teor_alcoolico
        self.disponibilidade = True

    def compra(self, idade_cliente):
        if self.disponibilidade and (self.tipo == "Não Alcoólico" or idade_cliente >= 18):
            self.disponibilidade = False
            return True
        return False

    def devolucao(self):
        self.disponibilidade = True


class Pagamento:
    @staticmethod
    def processar_pagamento():
        print("Pagamento processado com sucesso.")


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.compras_realizadas = []

    def fazer_compra(self, bebida):
        if bebida.compra(self.idade):
            self.compras_realizadas.append(bebida)
            Pagamento.processar_pagamento()
            return True
        self.imprimir_mensagem_compra_recusada(bebida)
        return False

    def devolver_bebida(self, bebida):
        bebida.devolucao()
        self.compras_realizadas.remove(bebida)

    def imprimir_mensagem_compra_recusada(self, bebida):
        if bebida.tipo == "Álcool" and self.idade < 18:
            print(f"{self.nome}, você não pode comprar {
                  bebida.nome} devido à idade.")
        else:
            print(f"{self.nome}, você não pode comprar {bebida.nome}.")

    def update(self, message):
        print(f"{self.nome}, você foi notificado: {message}")


class Armazem:
    def __init__(self):
        self.bebidas = []
        self.clientes = []

    def adicionar_bebida(self, bebida):
        self.bebidas.append(bebida)
        self.notify_observers(f"{bebida.nome} foi adicionada ao armazém.")

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_bebida(self, nome):
        return next((bebida for bebida in self.bebidas if bebida.nome.lower() == nome.lower()), None)


# Exemplo de uso interativo:
nome_cliente = input("Nome do cliente: ")
idade_cliente = int(input("Idade do cliente: "))

novo_cliente = Cliente(nome_cliente, idade_cliente)
armazem = Armazem()
armazem.cadastrar_cliente(novo_cliente)

# Mostrar as bebidas disponíveis após o cliente fornecer seu nome e idade
print("\nBebidas disponíveis:")
for bebida in armazem.bebidas:
    print(f"- {bebida.nome}")

nome_bebida_comprada = input("Nome da bebida que deseja comprar: ")
bebida_encontrada = armazem.buscar_bebida(nome_bebida_comprada)

if bebida_encontrada:
    if novo_cliente.fazer_compra(bebida_encontrada):
        print(f"{novo_cliente.nome} comprou {bebida_encontrada.nome}.")
        devolver_produto = input(
            "Gostaria de devolver algum produto? (s/n): ").lower()
        if devolver_produto == "s":
            # Devolução de bebida
            if novo_cliente.compras_realizadas:
                # Pega a primeira bebida comprada para devolver
                bebida_devolvida = novo_cliente.compras_realizadas[0]
                novo_cliente.devolver_bebida(bebida_devolvida)
                print(f"{novo_cliente.nome} devolveu {bebida_devolvida.nome}.")
                print(f"{novo_cliente.nome} realizou as seguintes compras após a devolução: {
                      [bebida.nome for bebida in novo_cliente.compras_realizadas]}")
            else:
                print(f"{novo_cliente.nome} não possui compras para devolver.")
    else:
        print(f"{novo_cliente.nome}, sua compra foi recusada.")
else:
    print(f"Bebida '{nome_bebida_comprada}' não encontrada no armazém.")

    adicionar_bebida = input(
        "Gostaria de adicionar esta bebida ao armazém? (s/n): ").lower()
    if adicionar_bebida == "s":
        tipo_bebida = input("Tipo da bebida (Álcool/Não Alcoólico): ")
        volume_ml = float(input("Volume (em mL): "))
        teor_alcoolico = float(
            input("Teor alcoólico (se for Álcool, caso contrário, digite 0): "))

        nova_bebida = Bebida(nome_bebida_comprada,
                             tipo_bebida, volume_ml, teor_alcoolico)
        armazem.adicionar_bebida(nova_bebida)
        print(f"{nova_bebida.nome} foi adicionada ao armazém com sucesso.")

        # Exibir o nome da bebida recém-adicionada
        print(f"{novo_cliente.nome} realizou as seguintes compras: {
              [bebida.nome for bebida in novo_cliente.compras_realizadas]}")
        print(f"Nova bebida adicionada ao armazém: {nova_bebida.nome}")
    else:
        print("Bebida não adicionada.")

print(f"{novo_cliente.nome} realizou as seguintes compras: {
      [bebida.nome for bebida in novo_cliente.compras_realizadas]}")
