cigarrosDiarios = int(input("\nInforme a quantidade de cigarros fumados diariamente: "))
anosFumando = int(input("Informe a quantidade de anos sendo fumante "))
cigarrosTotais = cigarrosDiarios * 365 * anosFumando
minutosPerdidos = cigarrosTotais * 10
diasPerdidos = minutosPerdidos / (24 * 60)
print(f"A expectativa de vida do fumante foi reduzida em {diasPerdidos:.2f} dias.")