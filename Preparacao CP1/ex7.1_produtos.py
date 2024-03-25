'''
Um vendedor necessita de um programa que calcule o preço total devido por um cliente. O algoritmo deve receber o código de um produto e a quantidade comprada e calcular o preço total, acrescendo o imposto que varia o seu percentual de acordo com o produto, usando a tabela abaixo:

Código do Produto	   Preço unitário		Percentual de imposto
      1001			       5,32			             18%
      1324			       6,45			             18%
      6548			       2,37			              6%
      0987			       5,32			              6%
      7623			       6,45			             12%
'''

# Definir os preços e as taxas de imposto dos produtos
preco_1001 = 5.32
taxa_imposto_1001 = 0.18
preco_1324 = 6.45
taxa_imposto_1324 = 0.18
preco_6548 = 2.37
taxa_imposto_6548 = 0.06
preco_0987 = 5.32
taxa_imposto_0987 = 0.06
preco_7623 = 6.45
taxa_imposto_7623 = 0.12

# Pegar o código do produto e a quantidade comprada pelo usuário
codigo_produto = str(input("\nInforme o código do produto(1001, 1324, 6548, 0987, 7623): "))
quantidade = int(input("Informe a quantidade comprada: "))

# Calcular o preço total e o imposto do produto informado
if codigo_produto == "1001":
    preco = preco_1001
    taxa_imposto = taxa_imposto_1001
elif codigo_produto == "1324":
    preco = preco_1324
    taxa_imposto = taxa_imposto_1324
elif codigo_produto == "6548":
    preco = preco_6548
    taxa_imposto = taxa_imposto_6548
elif codigo_produto == "0987":
    preco = preco_0987
    taxa_imposto = taxa_imposto_0987
elif codigo_produto == "7623":
    preco = preco_7623
    taxa_imposto = taxa_imposto_7623
else:
    print("Código de produto inválido.")
    exit()

subtotal = preco * quantidade
imposto = subtotal * taxa_imposto
total = subtotal + imposto

# Imprimir os resultados
print(f"\nValor unitário: R$ {preco:.2f}")
print(f"Porcentagem do Imposto: {taxa_imposto * 100:.1f}%")
print(f"Valor Total do Imposto: R$ {imposto:.2f}")
print(f"Valor Total: R$ {total:.2f}\n")