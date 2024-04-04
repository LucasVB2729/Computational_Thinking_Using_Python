I = int(input("\nDigite o valor de I (inteiro positivo): "))
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if I % 2 == 0:
    media_aritmetica = (A + B + C) / 3
    print(f"A média aritmética é: {media_aritmetica:.2f}\n")
elif I > 10:
    media_ponderada = (A * 2 + B * 3 + C * 4) / (2 + 3 + 4)
    print(f"A média aritmética ponderada é: {media_ponderada:.2f}\n")
else:
    print("Nenhuma das condições foi satisfeita.\n")