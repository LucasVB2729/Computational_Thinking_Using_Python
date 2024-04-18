def calcular_porcentagem(total, parte):
    if total == 0:
        return 0
    return (parte / total) * 100

def main():
    candidatos = {'1': 'Huguinho', '2': 'Zezinho', '3': 'Luizinho'}
    votos = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
    total_votos = 0
    total_nulos = 0
    total_brancos = 0

    while True:
        voto = input("\nDigite o código do candidato (1, 2, 3), 4 para voto nulo, 5 para voto em branco, ou 0 para encerrar: ")
        
        if voto == '0':
            break
        elif voto in candidatos.keys():
            votos[voto] += 1
            total_votos += 1
        elif voto == '4':
            total_nulos += 1
            total_votos += 1
        elif voto == '5':
            total_brancos += 1
            total_votos += 1
        else:
            print("Código inválido. Por favor, digite novamente.")

    print("\nResultado da Eleição:")
    for codigo, candidato in candidatos.items():
        print(f"{candidato}: {votos[codigo]} votos")

    print(f"Votos Nulos: {total_nulos}")
    print(f"Votos em Branco: {total_brancos}")
    print(f"Porcentagem de votos nulos sobre o total de votos: {calcular_porcentagem(total_votos, total_nulos):.2f}%")
    print(f"Porcentagem de votos em branco sobre o total de votos: {calcular_porcentagem(total_votos, total_brancos):.2f}%\n")

if __name__ == "__main__":
    main()