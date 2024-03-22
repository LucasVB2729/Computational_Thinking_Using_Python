velocidadeCarro = float(input("Insira a velociadade do carro: "))
excesso = (velocidadeCarro - 80)
multa = excesso * 5

if velocidadeCarro > 80:
    print(f"\nVocê foi multado!\nValor da multa {multa:.2f}\n")
else:
    print("\nContinue respeitando as regras de trânsito!\n")