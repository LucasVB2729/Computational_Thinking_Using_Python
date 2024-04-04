I = int(input("Digite o valor de I (inteiro positivo): "))
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# Verificação das condições e cálculo das médias
if I % 2 == 0:
    # Se I for par, calcular a média aritmética de A, B e C
    media_aritmetica = (A + B + C) / 3
    print("A média aritmética é:", media_aritmetica)
elif I > 10:
    # Se I for maior que 10, calcular a média aritmética ponderada de A, B e C
    media_ponderada = (A * 2 + B * 3 + C * 4) / (2 + 3 + 4)
    print("A média aritmética ponderada é:", media_ponderada)
else:
    print("Nenhuma das condições foi satisfeita.")