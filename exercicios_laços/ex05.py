# 5.Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 5 × 4 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
def multiplicacao(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = multiplicacao(num1, num2)
print(f"O resultado da multiplicação é: {resultado:.2f}\n")
