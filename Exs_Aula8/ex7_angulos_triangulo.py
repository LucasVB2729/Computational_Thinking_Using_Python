angulo1 = float(input("Digite o primeiro ângulo do triângulo: "))
angulo2 = float(input("Digite o segundo ângulo do triângulo: "))
angulo3 = float(input("Digite o terceiro ângulo do triângulo: "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("O triângulo é RETÂNGULO.")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("O triângulo é OBTUSÂNGULO.")
else:
    print("O triângulo é ACUTÂNGULO.")
