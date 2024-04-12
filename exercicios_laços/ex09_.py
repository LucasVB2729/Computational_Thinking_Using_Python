# 9. Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
def calcular_pagamento_divida(valor_divida, juro_mensal, pagamento_mensal):
    meses = 0
    total_pago = 0
    total_juros_pago = 0
    while valor_divida > 0:
        meses += 1
        juros_mes = valor_divida * juro_mensal
        total_juros_pago += juros_mes
        valor_divida += juros_mes
        valor_divida -= pagamento_mensal
        total_pago += pagamento_mensal
        if valor_divida < 0:
            valor_divida = 0
    return meses, total_pago, total_juros_pago

valor_divida = float(input("\nDigite o valor inicial da dívida: "))
juro_mensal = float(input("Digite o juro mensal (em decimal): "))
pagamento_mensal = float(input("Digite o valor mensal que será pago: "))
meses_para_pagar, total_pago, total_juros_pago = calcular_pagamento_divida(valor_divida, juro_mensal, pagamento_mensal)
print(f"Número de meses para pagar a dívida: {meses_para_pagar}")
print(f"Total pago: R${total_pago:.2f}")
print(f"Total de juros pago: R${total_juros_pago:.2f}\n")