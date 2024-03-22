salarioBruto = float(input("\nInforme seu salário: "))
if salarioBruto <= 1302.00:
    print(f"\nSalário Bruto: R${salarioBruto:.2f}\nINSS: R${(salarioBruto*7.5)/100:.2f}\nSalário Líquido: R${salarioBruto - ((salarioBruto*7.5)/100):.2f}\n")
elif salarioBruto >= 1302.01 and salarioBruto <= 2571.29:
    print(f"\nSalário Bruto: R${salarioBruto:.2f}\nINSS: R${(salarioBruto*9)/100:.2f}\nSalário Líquido: R${salarioBruto - ((salarioBruto*9)/100):.2f}\n")
elif salarioBruto >= 2571.29 and salarioBruto <= 3856.94:
    print(f"\nSalário Bruto: R${salarioBruto:.2f}\nINSS: R${(salarioBruto*12)/100:.2f}\nSalário Líquido: R${salarioBruto - ((salarioBruto*12)/100):.2f}\n")
else:
    print(f"\nSalário Bruto: R${salarioBruto:.2f}\nINSS: R${(salarioBruto*14)/100:.2f}\nSalário Líquido: R${salarioBruto - ((salarioBruto*14)/100):.2f}\n")