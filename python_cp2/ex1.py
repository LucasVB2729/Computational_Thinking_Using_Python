#As bananas custam R$ 0,50 cada se forem compradas menos do que uma dúzia, e R$ 0,40 se forem compradas pelo menos
#12. Escreve um programa que leia o número de bananas compradas e calcule o valor total da compra.

quantidade = int(input("\nInforme o número de bananas compradas: "))
valor = 0
if quantidade < 12:
    valor = 0.50 * quantidade
else:
    valor = 0.40 * quantidade
print(f"Bananas Compradas: {quantidade}\nValor Total: R$ {valor:.2f}\n")  