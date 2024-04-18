def cadastrar_usuario():
    while True:
        nome = input("\nNome: ")
        if len(nome) > 3:
            break
        else:
            print("O nome deve ter mais de 3 caracteres.")

    while True:
        try:
            idade = int(input("Idade: "))
            if 0 <= idade <= 150:
                break
            else:
                print("A idade deve estar entre 0 e 150 anos.")
        except ValueError:
            print("Idade inválida. Digite um número válido.")

    while True:
        try:
            salario = float(input("Salário: "))
            if salario > 0:
                break
            else:
                print("O salário deve ser maior que zero.")
        except ValueError:
            print("Salário inválido. Digite um número válido.")

    while True:
        sexo = input("Sexo (f/m): ").lower()
        if sexo == 'f' or sexo == 'm':
            break
        else:
            print("Sexo inválido. Digite 'f' para feminino ou 'm' para masculino.")

    while True:
        estado_civil = input("Estado Civil (s/c/v/d): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            break
        else:
            print("Estado civil inválido. Digite 's' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado.")

    print("\nCadastro realizado com sucesso:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
    estado_civil_descricao = {'s': 'Solteiro', 'c': 'Casado', 'v': 'Viúvo', 'd': 'Divorciado'}
    print(f"Estado Civil: {estado_civil_descricao[estado_civil]}")

def main():
    while True:
        cadastrar_usuario()
        continuar = input("\nDeseja cadastrar outro usuário? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado.\n")
            break

if __name__ == "__main__":
    main()