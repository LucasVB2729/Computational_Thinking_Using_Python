#Coleta de informações
valorCasa = float(input("\nInforme o valor da casa: "))
salario = float(input("Informe o seu salário: "))
anosPagar = float(input("Informe em quantos anos pretende pagar a casa: "))

#Cálculos de variáveis
mesesPagar = anosPagar * 12
parcelaMensal = valorCasa / mesesPagar
salarioPorcento = salario * 30 /100

#Validação para aprovação do empréstimo
if salarioPorcento >= parcelaMensal:
    print(f"O seu empréstimo foi aprovado! O valor da prestação mensal é R${parcelaMensal:.2f} e será cobrada durante {anosPagar:.0f} anos.\n")
else:
    print(f"\nSeu empréstimo foi negado! A parcela mensal tem um valor maior que 30% de seu salário.\n")