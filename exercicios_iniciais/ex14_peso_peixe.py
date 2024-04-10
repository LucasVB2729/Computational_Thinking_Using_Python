pesoPeixe = float(input("Informe quantos kilogramas de peixe João pescou: "))
excesso = (pesoPeixe - 50)
multa = excesso * 4
if excesso > 0:
    print(f"\nJoão pescou {pesoPeixe:.1f}kg de peixe, {excesso:.1f}kg a mais do que o permitido, portanto, deverá pagar uma multa de R${multa:.2f}.")
elif excesso <= 0:
    print(f"\nJoão pescou {pesoPeixe:.1f}kg de peixe e está dentro do permitido, portanto, não deverá pagar multa.")