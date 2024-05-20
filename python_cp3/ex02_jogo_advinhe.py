#2 - 1. Desenvolva um jogo de acerte o número, onde o computador escolhe um 
#número inteiro aleatório de 0 a 50, e o usuário tem 5 tentativas para 
#adivinhar o número, onde o aplicativo informa se é maior ou menor o 
#número.
#2. Implemente um sistema de pontuação com o seguinte comportamento: 
#se o usuário adivinhar o número na primeira tentativa, receberá a 
#pontuação máxima (ex. 100 pontos), 50 na segunda, 30 na terceira, 20 na 
#quarta; se o usuário adivinhar o número na última tentativa, receberá a 
#pontuação mínima (ex. 10 pontos); se o usuário não acertar o número, não 
#receberá nenhum ponto.
#3. Implemente um controle de erros. Caso o jogador digite um número fora 
#da faixa permitida ou caracteres não numéricos, o sistema deve notificar o 
#jogador e solicitar o input correto.
#4. Implemente a opção de o usuário iniciar uma nova partida. Ao finalizar 
#uma rodada, após o resultado final, o jogo deve perguntar se o jogador 
#quer iniciar uma nova partida e, em caso negativo, encerrar a aplicação.

import random

def jogo_acerte_o_numero():
    while True:
        # Escolha aleatória do número entre 0 e 50
        numero_secreto = random.randint(0, 50)
        tentativas_restantes = 5
        pontuacao_maxima = 100
        pontuacao = 0

        print("\nJogo de Acerte o Número!")
        print("Tente adivinhar o número entre 0 e 50.")

        while tentativas_restantes > 0:
            try:
                palpite = int(input(f"\nTentativa #{6 - tentativas_restantes}: "))
                if palpite < 0 or palpite > 50:
                    print("Por favor, insira um número entre 0 e 50.")
                    continue
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if palpite == numero_secreto:
                if tentativas_restantes == 5:
                    pontuacao = pontuacao_maxima
                elif tentativas_restantes == 4:
                    pontuacao = 50
                elif tentativas_restantes == 3:
                    pontuacao = 30
                elif tentativas_restantes == 2:
                    pontuacao = 20
                else:
                    pontuacao = 10

                print(f"Parabéns! Você acertou o número {numero_secreto} com {tentativas_restantes} tentativa(s) restante(s). Sua pontuação é: {pontuacao}")
                break
            elif palpite < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")

            tentativas_restantes -= 1
        else:
            print(f"\nSuas tentativas acabaram. O número era {numero_secreto}.")

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

jogo_acerte_o_numero()
