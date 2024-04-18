def adicao():
    for i in range(1, 11):
        print(f"1 + {i} = {1 + i}")

def subtracao():
    for i in range(1, 11):
        print(f"1 - {i} = {1 - i}")

def multiplicacao():
    for i in range(1, 11):
        print(f"1 * {i} = {1 * i}")

def divisao():
    for i in range(1, 11):
        print(f"1 / {i} = {1 / i}")

def exibir_menu():
    print("\nEscolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            adicao()
        elif opcao == "2":
            subtracao()
        elif opcao == "3":
            multiplicacao()
        elif opcao == "4":
            divisao()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()