#Escreva um programa que solicite números inteiros para o usuário. O programa deve ler os números até que o usuário 
#digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma, a média aritmética,
#o menor e maior número. Caso o usuário não digite um valor numérico o programa deverá informar que é número inválido.

quantidade = 0
while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    quantidade +=1
    if numero == 0:
        break

print(f"Números Inseridos: {quantidade -1}\nSoma: {(numero)}\nMédia Aritmética: {numero}\n")