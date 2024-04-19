j = 1
i = 0
nomes = []
saltos = []

while j == 1:
    nome = input(f"Digite o nome do {i+1}º competidor: ")
    if len(nome) >= 3:
        nomes.append(nome)
        saltos.append([float(input(f"Digite a distância do {i+1}º competidor no {j+1}º salto: ")) for j in range(5)])
        
        print(f"\nAtleta: {nomes[i]}\n")
        for idx, salto in enumerate(saltos[i], start=1):
            print(f"Salto {idx}: {salto} m")
            
        melhor_salto = max(saltos[i])
        pior_salto = min(saltos[i])
        saltos[i].remove(melhor_salto)
        saltos[i].remove(pior_salto)
        media = sum(saltos[i]) / len(saltos[i])
        
        print(f"\nMelhor salto: {melhor_salto} m")
        print(f"Pior salto: {pior_salto} m")
        print(f"Média dos demais saltos: {media} m\n")
        print(f"Resultado final: {nomes[i]}: {media} m\n")
        
        i += 1
        j = int(input("Digite 1 para continuar ou 0 para sair: "))
    else:
        print("Nome inválido\n")
print("Finalizando o programa...\n")