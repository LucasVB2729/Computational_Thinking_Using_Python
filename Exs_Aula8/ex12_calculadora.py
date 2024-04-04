numero1 = float(input("\nDigite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação você deseja realizar? (+ para soma, - para subtração, * para multiplicação, / para divisão): ")

if operacao == '+':
    resultado = numero1 + numero2
    print(f"Resultado da soma: {resultado:.2f}\n")
elif operacao == '-':
    resultado = numero1 - numero2
    print(f"Resultado da subtração: {resultado:.2f}\n")
elif operacao == '*':
    resultado = numero1 * numero2
    print(f"Resultado da multiplicação: {resultado:.2f}\n")
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado da divisão: {resultado:.2f}\n")
    else:
        print("Não é possível dividir por zero!\n")
else:
    print("Operação inválida! Por favor, escolha uma das operações: +, -, * ou /\n")
