num1 = float(input("\nInsira um valor: "))
maior = num1
num2 = float(input("Insira outro valor: "))
if num2 > maior:
    maior = num2
num3 = float(input("Insira outro valor: "))
if num3 > maior:
    maior = num3
print (f"\nO maior valor é: {maior}\n")
