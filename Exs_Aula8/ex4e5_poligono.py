num_lados = int(input("\nDigite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado do polígono (em cm): "))

if num_lados == 3:
    area = (medida_lado ** 2 * (3 ** 0.5)) / 4
    print("TRIÂNGULO")
    print(f"Área: {area:.2f}\n")
elif num_lados == 4:
    area = medida_lado ** 2
    print("QUADRADO")
    print(f"Área: {area:.2f}\n")
elif num_lados == 5:
    print("PENTÁGONO\n")
else:
    if num_lados < 3:
        print("NÃO É UM POLÍGONO\n")
    else:
        print("POLÍGONO NÃO IDENTIFICADO\n")
