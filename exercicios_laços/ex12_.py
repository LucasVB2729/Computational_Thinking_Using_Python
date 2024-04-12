# 12. Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.
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

def imprimir_primos(n):
    primos_encontrados = 0
    numero_atual = 2
    
    while primos_encontrados < n:
        if eh_primo(numero_atual):
            print(numero_atual, end=" ")
            primos_encontrados += 1
        numero_atual += 1

n = ler_numero()
print(f"Os primeiros {n} números primos são:")
imprimir_primos(n)