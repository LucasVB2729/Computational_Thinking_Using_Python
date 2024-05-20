#1 - Faça um programa com um menu que permita: 1. o usuário cadastrar 
#produtos: com código, nome, data de cadastro, valor de compra, valor de venda 
#e quantidade em estoque; 2. Cadastro de cliente, código, com nome, endereço 
#e email 3. deverá permitir a venda de itens, verificando o cliente, se o produto 
#existe e se tem em estoque; 4. exibir um relatório de produtos em estoque; 5. 
#relatório de vendas com vendas totais e lucros obtidos.

class Produto:
    def __init__(self, codigo, nome, data_cadastro, valor_compra, valor_venda, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.data_cadastro = data_cadastro
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.quantidade = quantidade

class Cliente:
    def __init__(self, codigo, nome, endereco, email):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.email = email

produtos = []
clientes = []
vendas = []

def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    data_cadastro = input("Digite a data de cadastro do produto: ")
    valor_compra = float(input("Digite o valor de compra do produto: "))
    valor_venda = float(input("Digite o valor de venda do produto: "))
    quantidade = int(input("Digite a quantidade em estoque do produto: "))
    produto = Produto(codigo, nome, data_cadastro, valor_compra, valor_venda, quantidade)
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def cadastrar_cliente():
    codigo = input("Digite o código do cliente: ")
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    email = input("Digite o email do cliente: ")
    cliente = Cliente(codigo, nome, endereco, email)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def realizar_venda():
    codigo_cliente = input("Digite o código do cliente: ")
    cliente = next((cliente for cliente in clientes if cliente.codigo == codigo_cliente), None)
    if cliente is None:
        print("Cliente não encontrado.")
        return

    codigo_produto = input("Digite o código do produto: ")
    produto = next((produto for produto in produtos if produto.codigo == codigo_produto), None)
    if produto is None:
        print("Produto não encontrado.")
        return

    quantidade_vendida = int(input("Digite a quantidade vendida: "))
    if quantidade_vendida > produto.quantidade:
        print("Quantidade insuficiente em estoque.")
        return

    produto.quantidade -= quantidade_vendida
    venda_total = quantidade_vendida * produto.valor_venda
    lucro_obtido = quantidade_vendida * (produto.valor_venda - produto.valor_compra) # Aqui estava multiplicando incorretamente
    vendas.append((cliente, produto, quantidade_vendida, venda_total, lucro_obtido))
    print("Venda realizada com sucesso!")

def relatorio_estoque():
    print("Relatório de produtos em estoque:")
    for produto in produtos:
        print(f"Código: {produto.codigo}, Nome: {produto.nome}, Quantidade em estoque: {produto.quantidade}")

def relatorio_vendas():
    vendas_totais = sum(venda[3] for venda in vendas)
    lucro_total = sum(venda[4] for venda in vendas)
    print("Relatório de vendas:")
    print(f"Vendas totais: R$ {vendas_totais}")
    print(f"Lucro total: R$ {lucro_total}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar produto")
        print("2. Cadastrar cliente")
        print("3. Realizar venda")
        print("4. Relatório de produtos em estoque")
        print("5. Relatório de vendas")
        print("6. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            cadastrar_cliente()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "4":
            relatorio_estoque()
        elif opcao == "5":
            relatorio_vendas()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()