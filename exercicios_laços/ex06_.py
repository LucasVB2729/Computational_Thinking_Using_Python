# 6. Escreva um programa que solicite números inteiros para o usuário. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
quantidade_numeros = 0
soma = 0
while True:
    numero = int(input("\nDigite um número inteiro (0 para sair): "))
    if numero == 0:
        break
    quantidade_numeros += 1
    soma += numero
if quantidade_numeros == 0:
    print("Nenhum número foi digitado.\n")
else:
    media = soma / quantidade_numeros
    print(f"Quantidade de números digitados: {quantidade_numeros}")
    print(f"Soma dos números digitados: {soma}")
    print(f"Média aritmética dos números digitados: {media}\n")