# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km/h acima de 80 km/h.

velocidadeCarro = float(input("Insira a velociadade do carro: "))
excesso = (velocidadeCarro - 80)
multa = excesso * 5

if velocidadeCarro > 80:
    print(f"\nVocê foi multado!\nValor da multa {multa:.2f}\n")
else:
    print("\nContinue respeitando as regras de trânsito!\n")