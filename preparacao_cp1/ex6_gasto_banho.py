# Escreva um programa que irá solicitar a quantidade de pessoas de uma residência e a quantidade de minutos em média que as pessoas se demoram no banho. Sabendo que o chuveiro é de 2400 W, o programa deverá calcular e exibir o consumo da energia elétrica, em quilowatt-hora no final do mês (30 dias) e o valor em reais gasto, dado que o valor do KWh é de R$ 0,40.

pessoasResidencia = int(input("\nInforma quantas pessoas moram na sua residência: "))
tempoChuveiro = float(input("Informe quantos minutos em média cada residente demora no banho por dia: "))
minutosBanhoDia = pessoasResidencia*tempoChuveiro
horasBanhoDia = minutosBanhoDia/60
gastokWh = ((2400*horasBanhoDia*30)/1000)
gastoReais = gastokWh * 0.40

print(f"\nConsumo Mensal de Energia do Chuveiro: {gastokWh:.2f} kWh\nCusto Mensal do Consumo: R$ {gastoReais:.2f}\n")