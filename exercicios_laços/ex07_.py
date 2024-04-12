# 7. Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
deposito_inicial = float(input("\nDigite o valor do depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
taxa_juros_decimal = taxa_juros / 100
total_ganho_juros = 0

for mes in range(1, 25):
    saldo_mes = deposito_inicial * (1 + taxa_juros_decimal) ** mes
    ganho_juros_mes = saldo_mes - deposito_inicial
    total_ganho_juros += ganho_juros_mes
    print(f"Após {mes} meses, o saldo é de R${saldo_mes:.2f} e o ganho de juros deste mês foi de R${ganho_juros_mes:.2f}.\n")
print(f"\nO total ganho com juros nos 24 meses foi de R${total_ganho_juros:.2f}.\n")
