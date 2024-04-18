def calcular_salario(salario_inicial, ano_atual):
    salario = salario_inicial
    percentual_aumento = 0.015  # 1.5% em 1996

    for ano in range(1996, ano_atual + 1):
        salario += salario * percentual_aumento
        percentual_aumento *= 2  # Aumento dobrado a cada ano

    return salario

def main():
    salario_inicial = 1000  # Salário inicial em 1995
    ano_atual = int(input("\nDigite o ano atual: "))

    salario_atual = calcular_salario(salario_inicial, ano_atual)

    print(f"O salário atual do funcionário em {ano_atual} é R$ {salario_atual:.2f}\n")

if __name__ == "__main__":
    main()