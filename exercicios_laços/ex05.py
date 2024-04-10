num1 = int(input("\nInforme um valor a ser somado: "))
num2 = int(input("Informe um outro valor a ser somado: "))
i = 0
while i <= num2:
    i += 1
    calculo = num1 + i
    print (f"{i}", end=" ")
print ("\nFim do laço")