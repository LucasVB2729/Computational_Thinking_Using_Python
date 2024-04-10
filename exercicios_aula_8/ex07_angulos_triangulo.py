angulo1 = float(input("\nDigite o primeiro ângulo do triângulo: "))
angulo2 = float(input("Digite o segundo ângulo do triângulo: "))
angulo3 = float(input("Digite o terceiro ângulo do triângulo: "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("O triângulo é RETÂNGULO.\n")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("O triângulo é OBTUSÂNGULO.\n")
else:
    print("O triângulo é ACUTÂNGULO.\n")