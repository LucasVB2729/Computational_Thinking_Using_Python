'''
Dado o salário de um funcionário, calcular o INSS correspondente segundo a tabela:
Salário (de)            Salário (até)	        Alíquota
0,00	                  1.302,00	              7,5%
1.302,01	              2.571,29	              9,0%
2571,30	                  3.856,94               12,0%
3.856,95	              7.507,49               14,0%

Salário: 1000
Salário Bruto: 1000
INSS: 75
Salário Líquido: 925

Caso o funcionário ganhe acima de 7507,49, não será calculado 14%, sim ele pagará o Teto que nada mais é do que 14% em cima do limite da última faixa.
'''

salarioBruto = float(input("\nInforme seu salário: "))
if salarioBruto <= 1302.00:
    print(f"\nSalário Bruto: R${salarioBruto:.2f}\nINSS: R${(salarioBruto*7.5)/100:.2f}\nSalário Líquido: R${salarioBruto - ((salarioBruto*7.5)/100):.2f}\n")
elif salarioBruto >= 1302.01 and salarioBruto <= 2571.29:
    print(f"\nSalário Bruto: R${salarioBruto:.2f}\nINSS: R${(salarioBruto*9)/100:.2f}\nSalário Líquido: R${salarioBruto - ((salarioBruto*9)/100):.2f}\n")
elif salarioBruto >= 2571.29 and salarioBruto <= 3856.94:
    print(f"\nSalário Bruto: R${salarioBruto:.2f}\nINSS: R${(salarioBruto*12)/100:.2f}\nSalário Líquido: R${salarioBruto - ((salarioBruto*12)/100):.2f}\n")
else:
    print(f"\nSalário Bruto: R${salarioBruto:.2f}\nINSS: R${(salarioBruto*14)/100:.2f}\nSalário Líquido: R${salarioBruto - ((salarioBruto*14)/100):.2f}\n")