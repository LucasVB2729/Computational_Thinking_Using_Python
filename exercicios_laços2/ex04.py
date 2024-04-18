def calcular_anos(populacao_A, taxa_crescimento_A, populacao_B, taxa_crescimento_B):
    anos = 0
    while populacao_A <= populacao_B:
        populacao_A *= 1 + taxa_crescimento_A / 100
        populacao_B *= 1 + taxa_crescimento_B / 100
        anos += 1
    return anos

def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, insira um número válido.")

def obter_populacao_e_taxa(mensagem_populacao, mensagem_taxa):
    while True:
        populacao = obter_numero(mensagem_populacao)
        taxa = obter_numero(mensagem_taxa)
        if taxa <= 0:
            print("A taxa de crescimento deve ser maior que zero.")
        else:
            return populacao, taxa

def main():
    while True:
        print("\nInforme as informações para os países:")
        populacao_A, taxa_crescimento_A = obter_populacao_e_taxa("População do país A: ", "Taxa de crescimento do país A (%): ")
        populacao_B, taxa_crescimento_B = obter_populacao_e_taxa("População do país B (deve ser maior que a população do país A): ", "Taxa de crescimento do país B (%): ")
        
        if populacao_A >= populacao_B:
            print("Erro: A população do país A deve ser menor que a do país B.")
            continue
        if taxa_crescimento_A <= taxa_crescimento_B:
            print("Erro: A taxa de crescimento do país A deve ser maior que a do país B.")
            continue
        
        anos_necessarios = calcular_anos(populacao_A, taxa_crescimento_A, populacao_B, taxa_crescimento_B)
        print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.")

        continuar = input("Deseja repetir a operação? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado.\n")
            break

if __name__ == "__main__":
    main()