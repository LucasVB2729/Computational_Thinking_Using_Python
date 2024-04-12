# 11. Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        # Verifica apenas os números ímpares até a raiz quadrada do número
        for i in range(3, int(numero ** 0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

def ler_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero < 0:
                print("Por favor, digite um número inteiro positivo.")
            else:
                return numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

numero = ler_numero()
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")