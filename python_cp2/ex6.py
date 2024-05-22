#Escreva um o programa solicite dois números para o usuário e exiba os números os números elevados ao quadrado, como 
#no exemplo: primeiro valor 2 e segundo valor 5.

num1 = int(input("\nDigite um número: "))
num2 = int(input("Digite outro número: "))

if num1 < num2:
    for num1 in range(num1, num2+1):
        print(f"{num1} ^ 2 = {num1**2}")
if num1 > num2:
    for num2 in range(num2, num1+1):
        print(f"{num2} ^ 2 = {num2**2}")
else:
    print(f"{num1} ^ 2 = {num1**2}")