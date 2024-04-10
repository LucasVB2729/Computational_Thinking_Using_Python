#Solicitar ganho por hora e horas mensais trabalhadas
salHora = float(input("\nInforme seu salário por hora: "))
horasMes = float(input("Informe quantas horas você trabalha por mês: "))

#Calculos salario e impostos
salBruto = float(f"{salHora * horasMes:.2f}")
calculoIR = float(f"{salBruto * 11 / 100:.2f}")
calculoINSS = float(f"{salBruto * 8 / 100:.2f}")
calculoSindicato = float(f"{salBruto * 5 / 100:.2f}")
salLiquido = float(f"{salBruto - calculoIR - calculoINSS - calculoSindicato:.2f}")

#Imprimir
print(f"\nSalário Bruto: {salHora * horasMes:.2f}")
print(f"Imposto de Renda: {salBruto * 11 / 100:.2f}")
print(f"Imposto Nacional do Seguro Social: {salBruto * 8 / 100:.2f}")
print(f"Valor Pago ao Sindicato: {salBruto * 5 / 100:.2f}")
print(f"Salário Líquido: {salBruto - calculoIR - calculoINSS - calculoSindicato:.2f}\n")