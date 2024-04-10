maximo = float('-inf')
minimo = float('inf')
soma = 0

for i in range(1, 11):
    numero = int(input(f"\nDigite o {i}º número inteiro: "))

    if numero > maximo:
        maximo = numero
    
    if numero < minimo:
        minimo = numero
    
    soma += numero
media = soma / 10

print(f"O valor máximo é: {maximo}")
print(f"O valor mínimo é: {minimo}")
print(f"O valor médio é: {media}\n")