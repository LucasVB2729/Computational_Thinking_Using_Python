pessoasResidencia = int(input("\nInforma quantas pessoas moram na sua residência: "))
tempoChuveiro = float(input("Informe quantos minutos em média cada residente demora no banho por dia: "))
minutosBanhoDia = pessoasResidencia*tempoChuveiro
horasBanhoDia = minutosBanhoDia/60
gastokWh = ((2400*horasBanhoDia*30)/1000)
gastoReais = gastokWh * 0.40

print(f"\nConsumo Mensal de Energia do Chuveiro: {gastokWh:.2f} kWh\nCusto Mensal do Consumo: R$ {gastoReais:.2f}\n")