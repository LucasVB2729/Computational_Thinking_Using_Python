lado1 = float(input("Digite a medida do primeiro lado do triângulo: "))
lado2 = float(input("Digite a medida do segundo lado do triângulo: "))
lado3 = float(input("Digite a medida do terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    print("O triângulo é EQUILÁTERO.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é ISÓSCELES.")
else:
    print("O triângulo é ESCALENO.")
