def fibonacci(n):
    sequencia = []
    num_anterior, num_atual = 0, 1
    for i in range(n):
        sequencia.append(num_anterior)
        num_anterior, num_atual = num_atual, num_anterior + num_atual
    return sequencia
numeros = int(input("Informe quantos números da Sequência de Fibonacci você deseja exibir: "))
resultado = fibonacci(numeros)
print({fibonacci})