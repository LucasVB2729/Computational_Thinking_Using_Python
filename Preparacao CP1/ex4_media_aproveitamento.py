nota1 = float(input("\nInforme a nota da sua primeira avaliação: "))
nota2 = float(input("Informe a nota da sua segunda avaliação: "))
nota3 = float(input("Informe a nota da sua terceira avaliação: "))
media = (nota1+nota2+nota3)/3
mediaAproveitamento = (nota1+(nota2*2)+(nota3*3)+media)/7 

print(f"\nA sua média de aproveitamento é {mediaAproveitamento:.1f}!\n")