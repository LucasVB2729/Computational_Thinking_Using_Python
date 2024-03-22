#Coletar informação
tempoMinutos = int(input("\nInforme a quantidade de minutos para converter em horas/minutos: "))

#Cálculo de horas e minutos
hora = tempoMinutos // 60
restoHora = tempoMinutos % 60
minutos = restoHora // 1
restoMinutos = restoHora % 1

#Impressão
print(f"{hora}h{minutos}m\n")