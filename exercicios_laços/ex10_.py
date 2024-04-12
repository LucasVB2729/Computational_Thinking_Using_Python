"""
10. Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:
Código		Preço
1 		0,50
2 		1,00
3 		4,00
5 		7,00
9 		8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro “Código inválido”.
"""

tabela_precos = {
    "1": 0.50,
    "2": 1.00,
    "3": 4.00,
    "5": 7.00,
    "9": 8.00
}

total_compra = 0
while True:
    codigo = input("\nDigite o código do produto (ou '0' para encerrar): ")
    if codigo == "0":
        break
    quantidade = int(input("Digite a quantidade comprada: "))
    if codigo in tabela_precos:
        preco_unitario = tabela_precos[codigo]
        preco_total = preco_unitario * quantidade
        total_compra += preco_total
        print(f"Produto {codigo}: R${preco_total:.2f}")
    else:
        print("Código inválido!")
print(f"Total da compra: R${total_compra:.2f}\n")