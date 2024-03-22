kilometrosRodados = float(input("\nInforme quantos Km's foram percorridos com o carro alugado: "))
diasAluguel = float(input("Informe a duração do aluguel em dias: "))
preço = (kilometrosRodados * 0.15) + (diasAluguel * 60)
print(f"\nO preço a se pagar pelo carro é R$ {preço:.2f}, sendo R$ {kilometrosRodados * 0.15:.2f} referente aos kilometros rodados e R$ {diasAluguel * 60:.2f} referente aos dias de aluguel.\n")