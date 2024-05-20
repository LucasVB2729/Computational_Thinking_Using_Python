valorProduto = float(input("\nInforme o valor do produto: "))
descontoPercentual = float(input("Informe o percentual de desconto do produto (apenas o número): "))
desconto = (descontoPercentual / 100) * valorProduto
valorFinal = valorProduto - desconto

print(f"\nValor do Produto: R${valorProduto:.2f}\nDesconto: R${desconto:.2f}\nValor Final: R${valorFinal:.2f}\n")