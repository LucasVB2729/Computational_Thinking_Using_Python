'''Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios (ME) que fazem parte da avaliação. Calcular a média de aproveitamento (MA), usando a fórmula: 
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
'''

nota1 = float(input("\nInforme a nota da sua primeira avaliação: "))
nota2 = float(input("Informe a nota da sua segunda avaliação: "))
nota3 = float(input("Informe a nota da sua terceira avaliação: "))
media = (nota1+nota2+nota3)/3
mediaAproveitamento = (nota1+(nota2*2)+(nota3*3)+media)/7 

print(f"\nA sua média de aproveitamento é {mediaAproveitamento:.1f}!\n")