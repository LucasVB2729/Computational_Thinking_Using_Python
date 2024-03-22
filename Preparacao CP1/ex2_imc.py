altura = float(input("\nInforme sua Altura: "))
peso = float(input("Informe seu Peso: "))
imc = peso / (altura*altura)

print(f"\nAltura: {altura}m\nPeso: {peso}kg\nIMC (Índice de Massa Corporal): {imc:.2f}kg/m²")
if imc < 16:
    print("Sua condição é: Baixo Peso Muito Grave!\n")
elif imc >= 16 and imc <= 16.99:
    print("Sua condição é: Baixo Peso Grave!\n")
elif imc >= 17 and imc <= 18.49:
    print("Sua condição é: Baixo Peso!\n")
elif imc >= 18.50 and imc <= 24.99:
    print("Sua condição é: Peso Normal!\n")
elif imc >= 25 and imc <= 29.99:
    print("Sua condição é: Sobrepeso!\n")
elif imc > 29.99:
    print("Sua condição é: Obesidade!\n")