def verificar_nota(gabarito):
    total_alunos = 0
    soma_notas = 0
    maior_acerto = 0
    menor_acerto = 10
    
    while True:
        respostas_aluno = input("Digite as respostas do aluno (ex: ABCDEE...): ").upper()
        
        if len(respostas_aluno) != 10:
            print("Por favor, digite exatamente 10 respostas.")
            continue
        
        total_alunos += 1
        acertos = sum(r1 == r2 for r1, r2 in zip(respostas_aluno, gabarito))
        soma_notas += acertos
        
        if acertos > maior_acerto:
            maior_acerto = acertos
        if acertos < menor_acerto:
            menor_acerto = acertos
        
        continuar = input("Outro aluno utilizará o sistema? (s/n): ")
        if continuar.lower() != 's':
            break
    
    media_notas = soma_notas / total_alunos if total_alunos != 0 else 0
    
    return maior_acerto, menor_acerto, total_alunos, media_notas

def cadastrar_gabarito():
    print("Digite as respostas do gabarito:")
    gabarito = [input(f"Resposta da questão {i + 1}: ").upper() for i in range(10)]
    return gabarito

def menu():
    gabarito = []
    while True:
        print("\n----- MENU -----")
        print("1. Cadastrar Gabarito")
        print("2. Verificar Notas dos Alunos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            gabarito = cadastrar_gabarito()
        elif escolha == '2':
            if not gabarito:
                print("Por favor, cadastre o gabarito primeiro.")
            else:
                maior_acerto, menor_acerto, total_alunos, media_notas = verificar_nota(gabarito)
                print("\n----- Resultados -----")
                print(f"Maior Acerto: {maior_acerto}")
                print(f"Menor Acerto: {menor_acerto}")
                print(f"Total de Alunos: {total_alunos}")
                print(f"Média das Notas da Turma: {media_notas}")
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
menu()
