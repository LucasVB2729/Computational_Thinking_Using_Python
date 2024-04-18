def verifica_palindromo(numero):
    numero_str = str(numero)
    numero_invertido = numero_str[::-1]
    
    if numero_str == numero_invertido:
        return True
    else:
        return False

def main():
    numero = int(input("\nDigite um número para verificar se é palíndromo: "))
    
    if verifica_palindromo(numero):
        print(f"O número {numero} é palíndromo.\n")
    else:
        print(f"O número {numero} não é palíndromo.\n")

if __name__ == "__main__":
    main()