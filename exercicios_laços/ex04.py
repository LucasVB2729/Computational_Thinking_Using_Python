# 4. Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
num = int(input("\nInsira com o valor: "))
i = 0
if num%2 == 1:
    i = 1
while i <= num:
    print (f"{i}", end=" ")
    i += 2
print("\nFim do laço\n")