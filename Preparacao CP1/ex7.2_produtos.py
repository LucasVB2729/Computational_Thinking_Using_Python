# Criação de uma lista
produtos = {
    int(1001): (5.32, 0.18),
    int(1324): (6.45, 0.18),
    int(6548): (2.37, 0.06),
    int("0987"): (5.32, 0.06),
    int(7623): (6.45, 0.12)
}

# Pegar o código do produto e a quantidade comprada pelo usuário
codigo_produto = int(input("\nInforme o código do produto(1001, 1324, 6548, 0987, 7623): "))
quantidade = int(input("Informe a quantidade comprada: "))

# Calcular o preço total e o imposto do produto informado
if codigo_produto not in produtos:
    print("Código de produto inválido.")
    exit()

preco, porcentagem_imposto = produtos[codigo_produto]
subtotal = preco * quantidade
imposto = subtotal * porcentagem_imposto
total = subtotal + imposto

# Imprimir os resultados
print(f"\nValor unitário: R$ {preco:.2f}")
print(f"Porcentagem do Imposto: {porcentagem_imposto * 100:.1f}%")
print(f"Valor Total do Imposto: R$ {imposto:.2f}")
print(f"Valor Total: R$ {total:.2f}\n")